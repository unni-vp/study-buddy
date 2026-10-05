// Local catalog keeps the viewer working on file:// and GitHub Pages alike.
(() => {
  const data = document.getElementById('mindmap-catalog');
  const dialog = document.getElementById('mindmap-dialog');
  if (!data || !dialog || !dialog.showModal) return;
  const maps = JSON.parse(data.textContent);
  const title = document.getElementById('mindmap-dialog-title');
  const canvas = dialog.querySelector('.mindmap-canvas');
  const stage = dialog.querySelector('.mindmap-stage');
  const image = document.getElementById('mindmap-full-image');
  const gallery = dialog.querySelector('.mindmap-modal-gallery');
  const galleryGrid = gallery.querySelector('.mindmap-grid');
  const zoom = document.getElementById('mindmap-zoom');
  const error = dialog.querySelector('.mindmap-load-error');
  const textLink = document.getElementById('mindmap-text-link');
  let selected = -1, scale = 1, fitting = true, opener = null, request = 0, drag = null;
  function revealTextVersion() {
    if (location.hash !== '#text-version') return;
    const text = document.getElementById('text-version');
    if (text) { text.open = true; text.querySelector('summary')?.focus(); }
  }
  revealTextVersion();
  window.addEventListener('hashchange', revealTextVersion);
  textLink.addEventListener('click', () => dialog.close());

  const controls = action => dialog.querySelector('[data-map-action="' + action + '"]');
  maps.forEach((map, index) => {
    const card = document.createElement('button');
    card.type = 'button'; card.className = 'mindmap-card';
    card.dataset.mindmapIndex = index;
    const preview = document.createElement('img');
    preview.src = map.thumbnail; preview.alt = ''; preview.className = 'mindmap-thumbnail';
    const label = document.createElement('strong'); label.textContent = map.title;
    card.append(preview, label); galleryGrid.append(card);
  });
  function ensureOpen(trigger) {
    if (dialog.open) return;
    opener = trigger || document.activeElement;
    dialog.showModal(); document.body.classList.add('mindmap-is-open');
    controls('close').focus();
  }
  function setScale(value, centre = true) {
    if (selected < 0 || !image.naturalWidth) return;
    const old = scale;
    const oldX = Math.max(0, (canvas.clientWidth - image.naturalWidth * old) / 2);
    const oldY = Math.max(0, (canvas.clientHeight - image.naturalHeight * old) / 2);
    const cx = (canvas.scrollLeft + canvas.clientWidth / 2 - oldX) / old;
    const cy = (canvas.scrollTop + canvas.clientHeight / 2 - oldY) / old;
    scale = Math.max(0.08, Math.min(3, value));
    const width = image.naturalWidth * scale, height = image.naturalHeight * scale;
    image.style.width = width + 'px'; image.style.height = height + 'px';
    stage.style.width = Math.max(canvas.clientWidth, width) + 'px';
    stage.style.height = Math.max(canvas.clientHeight, height) + 'px';
    zoom.textContent = Math.round(scale * 100) + '%';
    canvas.classList.toggle('is-zoomed', width > canvas.clientWidth || height > canvas.clientHeight);
    if (centre) {
      canvas.scrollLeft = cx * scale + Math.max(0, (canvas.clientWidth - width) / 2) - canvas.clientWidth / 2;
      canvas.scrollTop = cy * scale + Math.max(0, (canvas.clientHeight - height) / 2) - canvas.clientHeight / 2;
    } else { canvas.scrollLeft = 0; canvas.scrollTop = 0; }
  }
  function fit() {
    if (selected < 0 || !image.naturalWidth) return;
    fitting = true;
    setScale(Math.min((canvas.clientWidth - 20) / image.naturalWidth, (canvas.clientHeight - 20) / image.naturalHeight), false);
  }
  function showGallery(trigger) {
    request++; selected = -1;
    gallery.hidden = false; canvas.hidden = true; error.hidden = true;
    title.textContent = maps[0].title.replace(/ overview$/i, '') + ' mind maps';
    controls('gallery').hidden = true;
    dialog.querySelector('.mindmap-zoom-controls').hidden = true;
    controls('print').hidden = true; textLink.hidden = true;
    ensureOpen(trigger);
  }
  function showMap(index, trigger) {
    if (!maps[index]) return;
    const map = maps[index], token = ++request;
    selected = index; fitting = true;
    gallery.hidden = true; canvas.hidden = false; error.hidden = true;
    title.textContent = map.title; image.alt = map.title + ' revision map';
    controls('gallery').hidden = false;
    dialog.querySelector('.mindmap-zoom-controls').hidden = false;
    controls('print').hidden = false; textLink.hidden = false;
    textLink.href = map.page + '#text-version'; error.querySelector('a').href = map.page;
    ensureOpen(trigger);
    image.style.width = '0px'; image.style.height = '0px';
    image.onload = () => { if (token === request) fit(); };
    image.onerror = () => { if (token === request) { error.hidden = false; canvas.hidden = true; } };
    image.src = map.image;
    if (image.complete && image.naturalWidth) fit();
    // Replace focus when switching from a gallery card that just became hidden.
    if (gallery.contains(document.activeElement)) controls('gallery').focus();
  }
  document.addEventListener('click', event => {
    const action = event.target.closest('[data-map-action]');
    if (action && dialog.contains(action)) {
      const name = action.dataset.mapAction;
      if (name === 'close') dialog.close();
      else if (name === 'gallery') { showGallery(); galleryGrid.querySelector('button')?.focus(); }
      else if (name === 'fit') fit();
      else if (name === 'print') window.print();
      else if (name === 'actual') { fitting = false; setScale(1); }
      else if (name === 'in' || name === 'out') { fitting = false; setScale(scale * (name === 'in' ? 1.25 : 0.8)); }
      return;
    }
    const trigger = event.target.closest('[data-mindmap-gallery], [data-mindmap-index]');
    if (!trigger || (trigger.tagName === 'A' && (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey))) return;
    event.preventDefault();
    if (trigger.hasAttribute('data-mindmap-gallery')) showGallery(trigger);
    else showMap(Number(trigger.dataset.mindmapIndex), trigger);
  });
  dialog.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const items = [...dialog.querySelectorAll('button, a[href], [tabindex="0"]')]
      .filter(node => !node.disabled && node.getClientRects().length && getComputedStyle(node).visibility !== 'hidden');
    const first = items[0], last = items.at(-1);
    if (!first) return;
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault(); last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault(); first.focus();
    }
  });
  dialog.addEventListener('close', () => {
    request++; document.body.classList.remove('mindmap-is-open');
    opener?.focus(); opener = null; drag = null;
    canvas.classList.remove('is-dragging');
  });
  const resize = new ResizeObserver(() => {
    if (!dialog.open || selected < 0 || !image.naturalWidth) return;
    if (fitting) fit(); else setScale(scale);
  });
  resize.observe(canvas);
  canvas.addEventListener('wheel', event => {
    if (!event.ctrlKey || selected < 0) return;
    event.preventDefault(); fitting = false; setScale(scale * (event.deltaY < 0 ? 1.1 : 0.9));
  }, {passive:false});
  canvas.addEventListener('pointerdown', event => {
    if (event.pointerType !== 'mouse' || event.button !== 0 || !canvas.classList.contains('is-zoomed')) return;
    drag = {x:event.clientX, y:event.clientY, left:canvas.scrollLeft, top:canvas.scrollTop};
    canvas.setPointerCapture(event.pointerId); canvas.classList.add('is-dragging'); event.preventDefault();
  });
  canvas.addEventListener('pointermove', event => {
    if (!drag) return;
    canvas.scrollLeft = drag.left - event.clientX + drag.x;
    canvas.scrollTop = drag.top - event.clientY + drag.y;
  });
  const stopDrag = () => { drag = null; canvas.classList.remove('is-dragging'); };
  canvas.addEventListener('pointerup', stopDrag); canvas.addEventListener('pointercancel', stopDrag);
})();
