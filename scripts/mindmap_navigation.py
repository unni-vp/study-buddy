"""Clickable mind-map previews and shared illustrations for revision groups."""
from html import escape

CSS = '''.mindmap-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:22px 0}.mindmap-card{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:12px;background:white;border:1px solid #ccdcd6;border-radius:10px;text-decoration:none;text-align:center;color:#234c46}.mindmap-card:hover{background:#edf5f1;border-color:#28675d}.mindmap-card:focus-visible{outline:3px solid #cd9034;outline-offset:4px}.mindmap-card img{display:block;width:150px;max-width:100%;height:auto;aspect-ratio:4/3;object-fit:contain;border:1px solid #e0e7e3;border-radius:6px;background:#fffdf8}.mindmap-card strong{font-size:16px;line-height:1.35}.mindmap-card .map-arrow{display:none}.mindmap-view{margin:20px 0;background:white;border:1px solid #dce3e8;padding:12px;border-radius:12px}.mindmap-view img{display:block;width:100%;height:auto}.mindmap-view figcaption{font-size:18px;margin:10px 0}.mindmap-grid+footer{margin-top:20px}@media(max-width:1199px){.mindmap-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}@media(max-width:899px){.mindmap-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:720px){.mindmap-grid{gap:10px}.mindmap-card{padding:10px}.mindmap-card img{width:132px}.mindmap-card strong{font-size:15px}.mindmap-view{padding:4px}}'''

def icon(slug):
    if 'cell-process' in slug:
        body='<ellipse cx="90" cy="68" rx="72" ry="45" fill="#edf1fa" stroke="#276cad" stroke-width="3"/><path d="m54 46 14 22-14 22m72-44-14 22 14 22" stroke="#bd4160" stroke-width="6"/><path d="M85 68H40m55 0h45m-91-8-9 8 9 8m82-16 9 8-9 8" stroke="#25826c" stroke-width="3"/>'
    elif 'transport' in slug:
        body='<path d="M88 15v110m8-110v110" stroke="#8253ac" stroke-width="4"/><g fill="#276cad"><circle cx="28" cy="28" r="7"/><circle cx="55" cy="28" r="7"/><circle cx="28" cy="52" r="7"/><circle cx="55" cy="52" r="7"/><circle cx="132" cy="28" r="7"/></g><path d="M25 78h125m-12-12 12 12-12 12" stroke="#25826c" stroke-width="7"/><path d="M150 108H35m12-9-12 9 12 9" stroke="#bf7030" stroke-width="4"/>'
    elif 'exchange' in slug:
        body='<path d="M90 12v30m0 0L45 68m45-26 45 26m-45-26v58" stroke="#276cad" stroke-width="8"/><g fill="#e3f3f8" stroke="#276cad" stroke-width="3"><circle cx="43" cy="68" r="26"/><circle cx="137" cy="68" r="26"/><circle cx="64" cy="108" r="25"/><circle cx="116" cy="108" r="25"/></g><path d="M12 70c0 68 156 68 156 0" fill="none" stroke="#bd4160" stroke-width="5"/>'
    elif 'practical' in slug:
        body='<path d="m75 20 24 12-30 54-24-13z" fill="#e7f0fb" stroke="#276cad" stroke-width="4"/><path d="M105 47c44 10 38 62-8 67M35 96h64M90 114v12M32 127h113" stroke="#25826c" stroke-width="7" stroke-linecap="round"/><path d="M65 82v14" stroke="#8253ac" stroke-width="5"/><circle cx="119" cy="68" r="10" fill="#f8e0c3" stroke="#bf7030" stroke-width="3"/>'
    elif 'cell' in slug:
        body='<ellipse cx="90" cy="70" rx="75" ry="48" fill="#e7f0fb" stroke="#276cad" stroke-width="4"/><circle cx="66" cy="65" r="23" fill="#dac5eb" stroke="#8253ac" stroke-width="3"/><ellipse cx="127" cy="82" rx="24" ry="12" fill="#f8e0c3" stroke="#bf7030" stroke-width="3"/><path d="m110 82 8-6 8 12 8-12 8 6" stroke="#bf7030" stroke-width="2"/><g fill="#8253ac"><circle cx="109" cy="47" r="3"/><circle cx="87" cy="98" r="3"/><circle cx="48" cy="96" r="3"/></g>'
    else:
        body='<path d="M90 70 35 30m55 40 55-40m-55 40-55 40m55-40 55 40" stroke="#25826c" stroke-width="7"/><g fill="#e6f1ed" stroke="#25826c" stroke-width="3"><circle cx="90" cy="70" r="24"/><circle cx="35" cy="30" r="17"/><circle cx="145" cy="30" r="17"/><circle cx="35" cy="110" r="17"/><circle cx="145" cy="110" r="17"/></g>'
    return '<svg viewBox="0 0 180 140" fill="none" aria-hidden="true">'+body+'</svg>'

def card(href, title, thumbnail, index=None):
    trigger = f' data-mindmap-index="{index}"' if index is not None else ''
    return f'<a class="mindmap-card" href="{escape(href,quote=True)}"{trigger}><img class="mindmap-thumbnail" src="{escape(thumbnail,quote=True)}" alt="" width="200" height="150"><strong>{escape(title)}</strong><span class="map-arrow" aria-hidden="true">→</span></a>'
