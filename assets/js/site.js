/* Soft Ground portfolio — progressive enhancement only.
   Everything on the page is readable without this file. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- reveal on scroll ---------- */
  var revealEls = [].slice.call(document.querySelectorAll('.reveal'));
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- count-up on the headline metrics ---------- */
  var counters = [].slice.call(document.querySelectorAll('[data-count]'));
  function fmt(n, decimals) {
    var s = n.toFixed(decimals);
    var parts = s.split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
  }
  function countUp(el, delay) {
    var target = parseFloat(el.getAttribute('data-count'));
    var decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
    var animDecimals = parseInt(el.getAttribute('data-anim-decimals') || String(decimals), 10);
    var dur = 2200, start = null;
    el.textContent = fmt(0, animDecimals);
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var eased = 1 - Math.pow(1 - p, 4);           // fast start, long settle
      if (p < 1) { el.textContent = fmt(target * eased, animDecimals); requestAnimationFrame(step); }
      else { el.textContent = fmt(target, decimals); el.classList.add('counted'); }
    }
    setTimeout(function () { requestAnimationFrame(step); }, delay || 0);
  }
  var narrow = window.matchMedia && window.matchMedia('(max-width: 760px)').matches;
  /* numbers ticking up is content, not motion, so this also runs under prefers-reduced-motion */
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var group = e.target;
        cio.unobserve(group);
        var els = [].slice.call(group.querySelectorAll('[data-count]'));
        var base = group.classList.contains('hero-stats') ? 500 : 100;   // let the hero entrance land first
        els.forEach(function (el, i) { countUp(el, base + i * 160); });
      });
    }, narrow ? { rootMargin: '0px 0px -22% 0px', threshold: 0.2 }   // phones: wait until it is properly on screen
              : { threshold: 0.35 });
    var groups = [];
    counters.forEach(function (el) {
      var g = el.closest('.statbar') || el;
      if (groups.indexOf(g) === -1) { groups.push(g); cio.observe(g); }
    });
  } else if (counters.length) {
    counters.forEach(function (el, i) { countUp(el, 300 + i * 160); });
  }

  /* ---------- rotating role in the hero ---------- */
  var roles = [].slice.call(document.querySelectorAll('#role-rotator .roles span'));
  if (roles.length > 1 && !reduce) {
    var ri = 0, rolesBox = roles[0].parentNode;
    function fitRole() {                       // size the box to the active word so the text after it hugs it
      rolesBox.style.width = roles[ri].getBoundingClientRect().width + 'px';
    }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitRole); else fitRole();
    window.addEventListener('resize', fitRole);
    setInterval(function () {
      roles[ri].classList.remove('on'); roles[ri].classList.add('off');
      var prev = ri; ri = (ri + 1) % roles.length;
      roles[ri].classList.remove('off'); roles[ri].classList.add('on');
      fitRole();
      setTimeout(function () { roles[prev].classList.remove('off'); }, 520);
    }, 2800);
  }

  /* ---------- current section in the nav ---------- */
  var navLinks = [].slice.call(document.querySelectorAll('.nav a'));
  var sections = navLinks.map(function (a) { return document.querySelector(a.getAttribute('href')); }).filter(Boolean);
  if (sections.length && 'IntersectionObserver' in window) {
    var current = null;
    var nio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) current = e.target.id;
      });
      navLinks.forEach(function (a) {
        var on = a.getAttribute('href') === '#' + current;
        if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      });
    }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
    sections.forEach(function (s) { nio.observe(s); });
  }

  /* ---------- full-size report viewer ---------- */
  var zoomers = [].slice.call(document.querySelectorAll('[data-zoom]'));
  if (zoomers.length) {
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.innerHTML = '<div class="frame"><img alt=""></div><span class="hint">Scroll to read · Esc to close</span><button class="close" type="button" aria-label="Close">\u2715</button>';
    document.body.appendChild(box);
    var bimg = box.querySelector('img'), lastZoom = null;
    function openZoom(btn) {
      var src = btn.getAttribute('data-zoom');
      var inner = btn.querySelector('img');
      bimg.src = src;
      bimg.alt = inner ? inner.alt : '';
      box.classList.add('on');
      document.documentElement.style.overflow = 'hidden';
      lastZoom = btn;
      box.querySelector('.close').focus();
    }
    function closeZoom() {
      box.classList.remove('on');
      document.documentElement.style.overflow = '';
      if (lastZoom) lastZoom.focus();
    }
    zoomers.forEach(function (btn) { btn.addEventListener('click', function () { openZoom(btn); }); });
    box.addEventListener('click', function (e) { if (e.target === box || e.target.className === 'frame' || e.target.className === 'close') closeZoom(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && box.classList.contains('on')) closeZoom(); });
  }

  /* ---------- inquiry form (Netlify Forms, with a mailto fallback) ---------- */
  var form = document.getElementById('inquiry-form');
  if (form) {
    var status = document.getElementById('inquiry-status');
    var submit = document.getElementById('inquiry-submit');
    var TO = 'hello@isurumarasinghe.com';
    function fieldsOk() {
      var ok = true;
      [].slice.call(form.querySelectorAll('[required]')).forEach(function (el) {
        var valid = el.checkValidity();
        el.classList.toggle('invalid', !valid);
        if (!valid && ok) { el.focus(); ok = false; }
      });
      return ok;
    }
    function mailtoFallback(data) {
      var body = 'Name: ' + data.get('name') + '\nEmail: ' + data.get('email') + '\nContact number: ' + data.get('phone') + '\n\n' + data.get('inquiry');
      window.location.href = 'mailto:' + TO + '?subject=' + encodeURIComponent('Website inquiry from ' + data.get('name')) + '&body=' + encodeURIComponent(body);
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form-status';
      if (!fieldsOk()) { status.textContent = 'Please complete the highlighted fields.'; status.classList.add('err'); return; }
      var data = new FormData(form);
      submit.disabled = true; status.textContent = 'Sending…';
      var action = form.getAttribute('action') || '/';
      var isPhp = /\.php$/.test(action);
      var hosted = location.protocol === 'https:' || location.protocol === 'http:';
      var isPreview = /claude\.ai$/.test(location.hostname) || location.hostname === 'localhost' || location.hostname === '127.0.0.1';
      if (!hosted || (isPreview && !isPhp)) { submit.disabled = false; status.textContent = 'Opening your email app…'; mailtoFallback(data); return; }
      fetch(action, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json' }, body: new URLSearchParams(data).toString() })
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          return isPhp ? r.json() : { ok: true };
        })
        .then(function (res) {
          if (!res || res.ok === false) throw new Error('rejected');
          form.reset(); status.textContent = 'Thanks, your inquiry is on its way. I\'ll reply within one working day.'; status.classList.add('ok');
        })
        .catch(function () { status.textContent = 'Sending failed, so I\'ve opened your email app instead.'; status.classList.add('err'); mailtoFallback(data); })
        .then(function () { submit.disabled = false; });
    });
    form.addEventListener('input', function (e) { if (e.target.classList) e.target.classList.remove('invalid'); });
  }

})();
