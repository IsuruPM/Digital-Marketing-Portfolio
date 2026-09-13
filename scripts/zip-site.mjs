// Packages the deployable site into netlify-site.zip for drag-and-drop deploys.
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('..', import.meta.url));
const files = ['index.html', 'assets', 'Isuru-Marasinghe-Portfolio.pdf', 'netlify.toml', 'robots.txt'];
execSync(`cd "${root}" && rm -f netlify-site.zip && zip -qr netlify-site.zip ${files.join(' ')} -x "*/.gitkeep"`, { stdio: 'inherit' });
console.log('wrote netlify-site.zip');
