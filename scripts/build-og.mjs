// Renders print/og-card.html to the 1200x630 social share image.
import { chromium } from 'playwright';
import { execSync } from 'node:child_process';
// A sandbox or CI box may carry its own Chromium that does not match the version
// Playwright downloads. Point CHROMIUM_PATH at it to use that binary instead.
const launchOpts = process.env.CHROMIUM_PATH
  ? { executablePath: process.env.CHROMIUM_PATH, args: ['--headless', '--no-sandbox'] }
  : {};
const b = await chromium.launch(launchOpts);
const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 2 });
await p.goto('http://127.0.0.1:8765/print/og-card.html', { waitUntil: 'networkidle' });
await p.waitForTimeout(600);
await p.locator('.card').screenshot({ path: 'assets/img/og-cover.png' });
await b.close();
execSync(`python3 -c "
from PIL import Image
im=Image.open('assets/img/og-cover.png').convert('RGB').resize((1200,630), Image.LANCZOS)
im.save('assets/img/og-cover.jpg','JPEG',quality=90,optimize=True,progressive=True)
im.save('assets/img/og-cover.webp','WEBP',quality=88,method=6)
import os; os.remove('assets/img/og-cover.png')
print('og-cover', im.size, os.path.getsize('assets/img/og-cover.jpg')//1024, 'KB')
"`, { stdio: 'inherit' });
