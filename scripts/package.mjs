// Builds the two deployable file sets:
//   dist/netlify/         + netlify-site.zip          (Netlify Forms handles the inquiry form)
//   dist/shared-hosting/  + shared-hosting-site.zip   (contact.php handles it on any PHP host)
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const dist = join(root, 'dist');
rmSync(dist, { recursive: true, force: true });

const html = readFileSync(join(root, 'index.html'), 'utf8');

function base(dir) {
  mkdirSync(dir, { recursive: true });
  cpSync(join(root, 'assets'), join(dir, 'assets'), { recursive: true, filter: (src) => !src.endsWith('.gitkeep') });
  cpSync(join(root, 'robots.txt'), join(dir, 'robots.txt'));
  cpSync(join(root, 'sitemap.xml'), join(dir, 'sitemap.xml'));
  for (const f of ['favicon.ico','favicon-16x16.png','favicon-32x32.png','apple-touch-icon.png','android-chrome-192x192.png','android-chrome-512x512.png','site.webmanifest']) cpSync(join(root, f), join(dir, f));
}

// 1. Netlify: the page as-is (form action "/", data-netlify attributes) plus netlify.toml.
const netlify = join(dist, 'netlify');
base(netlify);
writeFileSync(join(netlify, 'index.html'), html);
cpSync(join(root, 'netlify.toml'), join(netlify, 'netlify.toml'));

// 2. Shared hosting: form posts to contact.php; Netlify attributes removed.
const shared = join(dist, 'shared-hosting');
base(shared);
const sharedHtml = html
  .replace('method="POST" action="/" data-netlify="true" netlify-honeypot="bot-field"', 'method="POST" action="contact.php"')
  .replace('<input type="hidden" name="form-name" value="inquiry">\n', '');
if (sharedHtml === html) throw new Error('form markup not found; packaging aborted');
writeFileSync(join(shared, 'index.html'), sharedHtml);
for (const f of ['contact.php', 'thanks.html', '.htaccess']) cpSync(join(root, 'hosting', 'shared', f), join(shared, f));

for (const [name, dir] of [['netlify-site.zip', netlify], ['shared-hosting-site.zip', shared]]) {
  execSync(`cd "${dir}" && rm -f "../${name}" && zip -qr "../${name}" . -x ".DS_Store"`, { stdio: 'inherit' });
  console.log('wrote dist/' + name);
}
