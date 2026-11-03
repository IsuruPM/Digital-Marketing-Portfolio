// Builds the two deployable file sets:
//   dist/netlify/         + netlify-site.zip          (Netlify Forms handles the inquiry form)
//   dist/shared-hosting/  + shared-hosting-site.zip   (contact.php handles it on any PHP host)
import { cpSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { execSync } from 'node:child_process';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const dist = join(root, 'dist');
rmSync(dist, { recursive: true, force: true });

const html = readFileSync(join(root, 'index.html'), 'utf8');
const caseFiles = readdirSync(root).filter((f) => /^(case-[a-z-]+|about)\.html$/.test(f));

// ---- cache busting -------------------------------------------------------
// netlify.toml caches CSS and JS for an hour and images for a week. Filenames do not
// change when their contents do, so a returning visitor keeps the old file until the
// cache expires: a fixed stylesheet or a re-cropped photograph simply does not arrive.
// Every asset reference in the HTML therefore gets ?v=<hash of the file>, which changes
// only when the file does and forces exactly the files that changed to be refetched.
const hashes = new Map();
function assetHash(dir, rel) {
  const key = dir + '|' + rel;
  if (hashes.has(key)) return hashes.get(key);
  const file = join(dir, rel);
  const h = existsSync(file)
    ? createHash('sha1').update(readFileSync(file)).digest('hex').slice(0, 8)
    : '';
  hashes.set(key, h);
  return h;
}

function bust(dir, text) {
  return text.replace(
    /((?:\.\.\/)?assets\/[A-Za-z0-9._\/-]+\.(?:css|js|jpg|jpeg|png|webp|svg|ico))/g,
    (match) => {
      const rel = match.replace(/^(?:\.\.\/)+/, '');
      const h = assetHash(dir, rel);
      return h ? match + '?v=' + h : match;
    });
}

function bustHtmlIn(dir) {
  let n = 0;
  const walk = (d) => {
    for (const entry of readdirSync(d, { withFileTypes: true })) {
      const p = join(d, entry.name);
      if (entry.isDirectory()) { if (entry.name !== 'assets') walk(p); continue; }
      if (!entry.name.endsWith('.html')) continue;
      const before = readFileSync(p, 'utf8');
      const after = bust(dir, before);
      if (after !== before) { writeFileSync(p, after); n++; }
    }
  };
  walk(dir);
  return n;
}

function base(dir) {
  mkdirSync(dir, { recursive: true });
  cpSync(join(root, 'assets'), join(dir, 'assets'), { recursive: true, filter: (src) => !src.endsWith('.gitkeep') });
  cpSync(join(root, 'robots.txt'), join(dir, 'robots.txt'));
  cpSync(join(root, 'sitemap.xml'), join(dir, 'sitemap.xml'));
  for (const f of ['favicon.ico','favicon-16x16.png','favicon-32x32.png','favicon-96x96.png','favicon.svg','apple-touch-icon.png','icon-192.png','icon-512.png','icon-maskable-512.png','site.webmanifest']) cpSync(join(root, f), join(dir, f));
}

// 1. Netlify: the page as-is (form action "/", data-netlify attributes) plus netlify.toml.
const netlify = join(dist, 'netlify');
base(netlify);
writeFileSync(join(netlify, 'index.html'), html);
for (const f of caseFiles) cpSync(join(root, f), join(netlify, f));
cpSync(join(root, 'services'), join(netlify, 'services'), { recursive: true });
cpSync(join(root, 'netlify.toml'), join(netlify, 'netlify.toml'));

// 2. Shared hosting: form posts to contact.php; Netlify attributes removed.
const shared = join(dist, 'shared-hosting');
base(shared);
const sharedHtml = html
  .replace('method="POST" action="/" data-netlify="true" netlify-honeypot="bot-field"', 'method="POST" action="contact.php"')
  .replace('<input type="hidden" name="form-name" value="inquiry">\n', '');
if (sharedHtml === html) throw new Error('form markup not found; packaging aborted');
writeFileSync(join(shared, 'index.html'), sharedHtml);
for (const f of caseFiles) cpSync(join(root, f), join(shared, f));
cpSync(join(root, 'services'), join(shared, 'services'), { recursive: true });
for (const f of ['contact.php', 'thanks.html', '.htaccess']) cpSync(join(root, 'hosting', 'shared', f), join(shared, f));

for (const dir of [netlify, shared]) console.log('cache-busted ' + bustHtmlIn(dir) + ' pages in ' + dir.split('/').pop());

for (const [name, dir] of [['netlify-site.zip', netlify], ['shared-hosting-site.zip', shared]]) {
  execSync(`cd "${dir}" && rm -f "../${name}" && zip -qr "../${name}" . -x ".DS_Store"`, { stdio: 'inherit' });
  console.log('wrote dist/' + name);
}
