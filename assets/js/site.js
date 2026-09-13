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
    var dur = 2000, start = null;
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
  if (counters.length && 'IntersectionObserver' in window && !reduce) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var group = e.target;
        cio.unobserve(group);
        var els = [].slice.call(group.querySelectorAll('[data-count]'));
        var base = group.classList.contains('hero-stats') ? 500 : 100;   // let the hero entrance land first
        els.forEach(function (el, i) { countUp(el, base + i * 160); });
      });
    }, { threshold: 0.35 });
    var groups = [];
    counters.forEach(function (el) {
      var g = el.closest('.statbar') || el;
      if (groups.indexOf(g) === -1) { groups.push(g); cio.observe(g); }
    });
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

  /* ---------- case dialog ---------- */
  var dialog = document.getElementById('case-dialog');
  var body = document.getElementById('case-body');
  var title = document.getElementById('case-title');
  var eyebrow = document.getElementById('case-eyebrow');
  var closeBtn = document.getElementById('case-close');
  var lastTrigger = null;
  var meta = {
    'leads':     { eyebrow: 'Case 01 · Meta Ads · UAE real estate', title: '5,364 property leads from one Meta account' },
    'closings':  { eyebrow: 'Case 02 · CRM · UAE real estate', title: 'From lead to closing: USD 22.1M in closed deals' },
    'meta-ecom': { eyebrow: 'Case 03 · Meta Ads · E-commerce', title: 'Purchase-optimised growth on Meta' },
    'google':    { eyebrow: 'Case 04 · Google Ads · E-commerce', title: 'Search and Shopping that pays for itself' },
    'klaviyo':   { eyebrow: 'Case 05 · Klaviyo · Lifecycle', title: 'Email revenue that grew while the list grew' }
  };
  function openCase(id, trigger) {
    var tpl = document.getElementById('tpl-' + id);
    if (!tpl || !dialog) return;
    body.innerHTML = '';
    body.appendChild(tpl.content.cloneNode(true));
    title.textContent = (meta[id] || {}).title || '';
    eyebrow.textContent = (meta[id] || {}).eyebrow || '';
    lastTrigger = trigger || null;
    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    } else {
      dialog.setAttribute('open', '');
    }
    dialog.querySelector('.case-inner').scrollTop = 0;
    closeBtn.focus();
    root.style.overflow = 'hidden';
  }
  function closeCase() {
    if (!dialog) return;
    if (dialog.open) dialog.close(); else dialog.removeAttribute('open');
  }
  if (dialog) {
    [].slice.call(document.querySelectorAll('[data-case]')).forEach(function (btn) {
      btn.addEventListener('click', function () { openCase(btn.getAttribute('data-case'), btn); });
    });
    closeBtn.addEventListener('click', closeCase);
    dialog.addEventListener('click', function (e) {
      // click on the backdrop (outside the inner panel) closes
      var r = dialog.getBoundingClientRect();
      var inside = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
      if (!inside) closeCase();
    });
    dialog.addEventListener('close', function () {
      root.style.overflow = '';
      if (lastTrigger) lastTrigger.focus();
    });
  }

  /* ---------- inquiry form (Netlify Forms, with a mailto fallback) ---------- */
  var form = document.getElementById('inquiry-form');
  if (form) {
    var status = document.getElementById('inquiry-status');
    var submit = document.getElementById('inquiry-submit');
    var TO = 'isurupm1997@gmail.com';
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
