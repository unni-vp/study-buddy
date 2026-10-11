"""Readable landscape maps of writing decisions, not device checklists."""
from english_language_writing_notes import ROOT,TOPIC
from biology_course_maps import p,m
import a4_mindmaps as a4
import subprocess,json
from pathlib import Path
MAPS=[
m('00-writing-overview','Transactional writing',['Choose your direction','Develop & connect','Shape & check'],[
p('A job for the reader','**Purpose:** inform, advise, argue, persuade, discuss or review. Decide what the reader should understand or do.','**Audience + form + tone** shape your choices. An advice article needs help, not a sales pitch.'),
p('Protect both tasks','Two compulsory tasks: **20 marks each**. Communication/organisation 12; language accuracy 8.','Recent papers suggest 300–400 words and 30 minutes each. Plan, write and leave checking time.'),
p('Ideas need substance','Choose distinct points. Ask **why, how, what example, what consequence?**','A few developed ideas are stronger than repeating a general claim. Use credible details, not invented research.'),
p('Give paragraphs jobs','Opening → clear direction. Middle → develop ideas in a useful order. Ending → judgement, recommendation or next step.','**Coherence:** whole piece makes sense. **Cohesion:** its parts connect.'),
p('Voice & form','Article: headline and connected prose. Letter: greeting, purpose and sign-off. Speech: words listeners can follow.','Review: detail + judgement + reasons. Advice: action + how + why. Adapt register to the reader.'),
p('Control, then edit','Use precise vocabulary and varied sentences for meaning. Devices must serve the idea.','Check relevance, development, paragraph links, tone, sentence boundaries, agreement, tense and spelling.')]),
m('01-planning-and-development','Planning & development',['Read the task','Build the substance','Choose the route'],[
p('Decode the request','Identify **form, audience, purpose and context**. Use a supplied title.','Write: “I want this reader to ... because ...”. Do not change the task to fit a memorised answer.'),
p('Select a clear position','For an argument, decide your main claim. For advice, decide the useful action; for review, your judgement.','Consider the reader’s needs and worries. An editor can publish views, but cannot personally change a school rule.'),
p('Different points','For clubs: learning a skill, meeting people, fitting attendance around commitments.','Three versions of “clubs are fun” are repetition. Each paragraph should add something new.'),
p('Develop one point','**Point → detail → explanation → reader.** Use this as a thinking route, not a fixed formula.','Example: small coding task → visible success → unfamiliar skills feel learnable. Explain the connection.'),
p('Order paragraph jobs','Persuade: concern → benefits → obstacle and response → action.','Advise: preparation → first action → likely difficulty → next step. Discuss: weigh views → reasoned judgement.'),
p('Plan quickly','Use brief paragraph notes and one useful example for each key point. No compulsory paragraph count.','Check that the ending follows from the plan. Keep time to draft and edit both tasks.')]),
m('02-articles-and-persuasion','Articles & persuasion',['Invite the reader in','Make the case','Leave a clear direction'],[
p('Headline & opening','Use a headline that reveals the angle. Begin with a relevant moment, contrast or focused question.','Reach the subject quickly. A long fictional story can take over an article.'),
p('Write for these readers','School magazine: familiar situations and a lively, respectful voice. Formal publication: adapt the register.','Direct address can involve readers. Avoid blaming them or assuming everyone has the same life.'),
p('Develop paragraphs','One main idea → concrete example → why it matters. Change paragraph when the job or focus changes.','Connect naturally: “This small change ...”, “Another difficulty ...”, “That benefit ...”.'),
p('Use devices deliberately','A question sharpens an issue; a contrast clarifies a choice; a three-part pattern gives rhythm.','Reasons support persuasion. Techniques express them. Do not force every device into every piece.'),
p('Handle a real objection','**Concede → respond → justify.** Accept a valid concern and give a workable answer.','“After-school travel is difficult; a lunchtime trial offers another route.” Avoid dismissing opponents.'),
p('A purposeful close','Bring the message together. Return to an opening image or give a practical next step.','“Choose one room, one lunchtime and one chance.” Do not introduce a major new argument at the end.')]),
m('03-forms-and-audiences','Forms & audiences',['Recognise the form','Match voice to reader','Support useful judgements'],[
p('Article or guide','Article: headline, engaging opening, developed paragraphs and an ending with a purpose.','Guide: organise around the reader’s needs. **Action + how + why** turns a tip into useful advice.'),
p('Letter','State why you are writing, develop the case, finish with an appropriate request or conclusion.','Named recipient: Yours sincerely. Unknown: Yours faithfully. Be firm and courteous; challenge ideas, not people.'),
p('Speech or talk','Address listeners and use words that sound natural aloud. Signpost changes so listeners can follow.','Short emphasis can follow a longer explanation. A talk is written speech, not a list of stage directions.'),
p('Review','**Detail + judgement + reason.** Choose criteria such as accessibility, atmosphere, quality or value.','Give strengths and limitations; recommend for a named type of reader. Avoid retelling the entire plot.'),
p('Report or leaflet','Report: purpose → grouped findings → implications → recommendation if requested.','Leaflet: clear sections with useful developed information. Headings help navigation; decoration does not replace content.'),
p('Adapt the same idea','To a friend: warm and direct. To a headteacher: respectful, clear and specific.','Keep the main purpose in view. Match details to what the reader can know, value and realistically do.')]),
m('04-style-and-editing','Style & editing',['Choose precise language','Control the sentences','Improve the whole piece'],[
p('Precision','“The fee excludes students on tight budgets” is clearer than “It is really, really bad”.','Use words accurately. Qualify claims when needed: can, may, some. Avoid unsupported “everyone” or “always”.'),
p('Controlled persuasion','Vary pace: longer sentences explain; short sentences emphasise. “Neither sounds spectacular. Both matter.”','Use emotion proportionately. A brief example can be more convincing than a dramatic exaggeration.'),
p('Sentence boundaries','Comma splice: “It is free, everyone can try it.”','Repair with a full stop, a semicolon between complete clauses, or a conjunction: “It is free, so everyone can try it.”'),
p('Punctuation & grammar','Colon after a complete clause introduces explanation. Apostrophe marks possession or omitted letters.','Its = possession; it’s = it is/has. Their = possession; they’re = they are. Check agreement and tense.'),
p('Meaning first','Does every paragraph add a distinct idea? Have you explained how or why with a concrete detail?','Does the order make sense? Does the ending fulfil the task? Keep the tone suitable when disagreeing.'),
p('Accuracy pass','Check sentence boundaries, spelling, apostrophes, tense and agreement. Use spellings printed in the task correctly.','Replace vague repetition with an example. Keep checking time for both responses; do not perfect only the first.')])]

def route(w,labels):
 b='';colours=['#2166ad','#7750a1','#18837b'];x=0
 # Stack each step to preserve legibility in narrow panels.
 for i,label in enumerate(labels):
  y=i*40
  b+=f'<rect x="5" y="{y}" width="{w-10}" height="27" rx="6" fill="#edf4fb" stroke="{colours[i%3]}"/>'+a4.text(w/2,y+19,label,15,anchor='middle',cls='diagram-label')
  if i<len(labels)-1:b+=f'<path d="M{w/2} {y+28}v10m-4-4 4 4 4-4" fill="none" stroke="#526e83" stroke-width="2"/>'
 return b
base=a4.illustration
def illustration(kind,w,h):
 routes={'writing-route':['Purpose','Reader','Writing choices'],'develop-route':['Claim','Example + explanation','Why it matters'],'argument-route':['Acknowledge concern','Offer a response','Explain why it works'],'review-route':['Specific feature','Its effect','Who it suits'],'editing-route':['Improve the meaning','Check the sentences','Proofread the details']}
 return route(w,routes[kind]) if kind in routes else base(kind,w,h)
a4.illustration=illustration
PICS=[{0:('writing-route',120)},{3:('develop-route',120)},{4:('argument-route',120)},{3:('review-route',120)},{4:('editing-route',120)}]

def build():
 f=TOPIC/'Mind Maps';f.mkdir(exist_ok=True);paths=[]
 for i,item in enumerate(MAPS):
  key='english-writing-'+item['slug'];a4.COMPACT[key]=item['panels'];a4.PLANS[key]=([[0,1],[2,3],[4,5]],item['labels'],PICS[i]);out=f/(item['slug']+'.svg')
  out.write_text(a4.build_a4(dict(item,slug=key)),encoding='utf-8');paths.append(str(out))
  out.with_suffix('.md').write_text('# '+item['title']+'\n\n'+'\n\n'.join('## '+p['title']+'\n\n'+'\n'.join('- '+x for x in p['lines']) for p in item['panels'])+'\n',encoding='utf-8')
 node=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 subprocess.run([str(node),str(ROOT/'scripts/render_mindmap_previews.cjs'),*paths],cwd=ROOT,check=True)
 p=TOPIC/'resource-coverage.json';d=json.loads(p.read_text());d['mindmaps']=[m['slug'] for m in MAPS];p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
if __name__=='__main__':build()
