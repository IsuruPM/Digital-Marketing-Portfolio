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
  function countUp(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
    var dur = 1100, start = null;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * eased, decimals);
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = fmt(target, decimals);
    }
    requestAnimationFrame(step);
  }
  if (counters.length && 'IntersectionObserver' in window && !reduce) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { countUp(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
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
    'closings':  { eyebrow: 'Case 02 · CRM · UAE real estate', title: 'From lead to closing' },
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
})();
