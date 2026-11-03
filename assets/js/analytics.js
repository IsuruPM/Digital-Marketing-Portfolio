/* Google tag configuration, in a file of its own so the Content-Security-Policy does
   not have to allow inline scripts. The loader itself stays in the page head as an
   ordinary external script from googletagmanager.com. */
window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push(arguments); }
gtag('js', new Date());
gtag('config', 'G-307CN46RYD');
