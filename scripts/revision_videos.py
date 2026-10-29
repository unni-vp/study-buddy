"""Render optional video collections using reviewed publisher embed addresses."""
import json,re
from html import escape as esc

def build_video_page(source,target,subject,topic,topicpage,write,link):
 data=json.loads(source.read_text(encoding='utf-8'));items=[]
 for video in data['videos']:
  embed=video['embed_url'];watch=video['watch_url']
  if not re.fullmatch(r'https://www\.youtube-nocookie\.com/embed/[A-Za-z0-9_-]{11}',embed):
   raise ValueError('Unreviewed embed host or video ID: '+embed)
  if not re.fullmatch(r'https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}',watch):
   raise ValueError('Invalid watch link: '+watch)
  title=esc(video['title']);provider=esc(video['provider'])
  items.append(f'<article class="revision-video"><h2>{title}</h2><div class="video-stage" data-video-embed="{esc(embed)}" data-video-title="{title}"><button class="video-load" type="button" aria-label="Watch {title}"><svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21"/><path d="m20 15 14 9-14 9Z"/></svg><span>Watch video</span></button></div><p class="video-provider">{provider} · <a href="{esc(watch)}" target="_blank" rel="noopener noreferrer">Open on YouTube<span class="sr-only">: {title}</span></a></p></article>')
 content=(f'<div class="reader-tools"><a href="{link(target,topicpage)}">← Back to topic</a></div>'
          f'<h1>{esc(data["title"])}</h1><div class="revision-video-grid">'+''.join(items)+'</div>'
          f'<script defer src="{link(target,target.parent.parent/"videos.js")}"></script>')
 write(target,data['title'],content,[(subject.split(' - ')[0],topicpage.parents[1]/'index.html'),(topic,topicpage)],subject)
 return target,f'{len(items)} revision videos'
