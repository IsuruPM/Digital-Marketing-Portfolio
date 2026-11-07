# Ready-to-upload site

`public_html/` is the built site for shared hosting, exactly as it should appear
in your hosting account's web root. It is committed so it can be pulled straight
onto the server when a browser upload of the zip fails.

From cPanel Terminal (or SSH):

    cd ~
    git clone --depth 1 -b claude/amazing-planck-hce9v0 \
      https://github.com/IsuruPM/Digital-Marketing-Portfolio.git tmpsite
    cp -a tmpsite/deploy/public_html/. ~/isurumarasinghe.com/
    rm -rf tmpsite

`cp -a` copies the dotfiles too, which matters: without `.htaccess` every clean
URL returns 404 and the www redirect never fires.

Regenerate with `npm run package`, then copy `dist/shared-hosting` over this
folder.
