// Renders print/deck.html to Isuru-Marasinghe-Portfolio.pdf (1440 × 810 pages).
// Usage: node scripts/build-pdf.mjs   (needs `playwright` and a Chromium it can find)
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';

const root = fileURLToPath(new URL('..', import.meta.url));
const out = join(root, 'Isuru-Marasinghe-Portfolio.pdf');
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.jpg': 'image/jpeg', '.png': 'image/png', '.woff2': 'font/woff2', '.svg': 'image/svg+xml' };

const server = createServer(async (req, res) => {
  try {
    const path = normalize(join(root, decodeURIComponent(req.url.split('?')[0])));
    if (!path.startsWith(root)) throw new Error('outside root');
    const s = await stat(path);
    const file = s.isDirectory() ? join(path, 'index.html') : path;
    res.writeHead(200, { 'content-type': types[extname(file)] || 'application/octet-stream' });
    res.end(await readFile(file));
  } catch {
    res.writeHead(404); res.end();
  }
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const port = server.address().port;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 810 } });
await page.goto(`http://127.0.0.1:${port}/print/deck.html`, { waitUntil: 'networkidle' });
await page.evaluate(async () => {
  await document.fonts.ready;
  await Promise.all([...document.images].map((img) => img.complete ? null : new Promise((r) => { img.onload = img.onerror = r; })));
});
await page.pdf({ path: out, width: '1440px', height: '810px', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
await browser.close();
server.close();
console.log('wrote', out);
