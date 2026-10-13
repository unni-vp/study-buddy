"""Build one Literature topic with the approved readable panel layout."""
from literature_helpers import ROOT,SUBJECT,TOPICS
from literature_maps import MAPS
from readable_subject_mindmaps import build as build_readable
import sys, json

def build(n):
    folder = ROOT / SUBJECT / TOPICS[n-1] / 'Mind Maps'
    for item in MAPS[n]:
        lines = ['# ' + item['title']]
        for panel in item['panels']:
            lines += ['## ' + panel['title'], '\n'.join('- ' + line for line in panel['lines'])]
        (folder / (item['slug'] + '.md')).write_text('\n\n'.join(lines) + '\n', encoding='utf-8')
    build_readable(SUBJECT,TOPICS,MAPS,n)
    review_path = folder.parent / 'mindmap-layout-review.json'
    review = json.loads(review_path.read_text(encoding='utf-8'))
    review['full_text'] = 'Editable Markdown counterparts synchronised with the same maintained map definitions.'
    review_path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
if __name__=='__main__':build(int(sys.argv[1]))
