"""Reusable offline full-screen viewer with ordinary-link fallbacks."""
from html import escape
import json

def viewer_markup(page, catalog, link):
    maps=[{'title':m['title'],'image':link(page,m['image']),'thumbnail':link(page,m['thumbnail']),'page':link(page,m['page'])} for m in catalog]
    data=json.dumps(maps,ensure_ascii=False).replace('<',chr(92)+'u003c')
    return ('<script type="application/json" id="mindmap-catalog">'+data+'</script>'
      '<dialog class="mindmap-dialog" id="mindmap-dialog" aria-labelledby="mindmap-dialog-title">'
      '<div class="mindmap-toolbar"><h2 id="mindmap-dialog-title">Mind maps</h2>'
      '<div class="mindmap-controls"><button type="button" data-map-action="gallery">← All maps</button>'
      '<span class="mindmap-zoom-controls"><button type="button" data-map-action="out" aria-label="Zoom out">−</button>'
      '<output id="mindmap-zoom" aria-label="Zoom level" aria-live="polite">100%</output>'
      '<button type="button" data-map-action="in" aria-label="Zoom in">+</button>'
      '<button type="button" data-map-action="fit">Fit</button><button type="button" data-map-action="actual">100%</button></span>'
      '<a id="mindmap-text-link" href="#">Text version</a><button type="button" data-map-action="print">Print</button>'
      '<button type="button" data-map-action="close" aria-label="Close mind map">Close ×</button></div></div>'
      '<div class="mindmap-modal-gallery"><div class="mindmap-grid"></div></div>'
      '<div class="mindmap-canvas" tabindex="0" aria-label="Mind map; use zoom buttons and scroll to explore">'
      '<div class="mindmap-stage"><img id="mindmap-full-image" alt="" draggable="false"></div></div>'
      '<p class="mindmap-load-error" role="alert" hidden>Unable to load this map. <a href="#">Open the map page</a></p>'
      '</dialog>')
