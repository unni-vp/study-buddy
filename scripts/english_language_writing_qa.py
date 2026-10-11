"""Original writing practice and fully developed example responses."""
from english_language_writing_notes import TOPIC,TITLE
import json,re
ITEMS=[]
def q(mark,prompt,answer,focus):
 # Short examples use a blank paragraph before their teaching commentary.
 if mark < 20 and '\n\n' in answer:
  answer=answer.replace('\n\n','\n\n---\n\n',1)
 ITEMS.append(dict(marks=mark,prompt=prompt,answer=answer,focus=focus))
q(1,'What does audience mean in a writing task?','The intended readers or listeners.','Audience')
q(1,'What is register?','The level of formality in the language.','Register')
q(1,'How many writing tasks must you complete in Component 2 Section B?','Two.','Exam structure')
q(1,'Name the main weakness in this claim: “Every student who joins a club will become successful.”','Overgeneralisation.','Credible claims')
q(1,'What is a counterargument?','A reasonable objection or opposing argument.','Argument')
q(1,'Which word completes the sentence: “The club has changed ___ meeting time”—its or it\'s?','Its.','Accuracy')
q(2,'An article must advise new Year 7 students about joining clubs. Identify its audience and main purpose.','- Audience: **new Year 7 students**.\n- Purpose: **give useful advice** about choosing and joining clubs.','Purpose and audience')
q(2,'Explain why “Clubs are fun. Clubs are enjoyable” does not develop the idea.','- Both sentences repeat essentially the **same claim**.\n- Neither gives a **specific example or explanation** of what makes the experience enjoyable.','Development')
q(2,'Replace “This ridiculous rule proves you are useless” with a firm but respectful sentence to a headteacher.','“I am concerned that this rule prevents students with long journeys home from attending clubs, and I would welcome a lunchtime alternative.”\n\nIt challenges the **rule and its consequence**, while keeping the tone **courteous**.','Tone')
q(2,'Correct the two errors in “The students was excited to visit there new library.”','“The students **were** excited to visit **their** new library.”','Agreement and spelling')
q(2,'Repair the comma splice in “The session is free, everyone can try it” in two different ways.','- “The session is free. Everyone can try it.”\n- “The session is free, so everyone can try it.”','Sentence boundaries')
q(2,'Why might a paragraph about low prices need a different example in a review for families than in a review for teenagers?','- Families may care about **the total cost for several people**, including children.\n- Teenagers may be more concerned about **their own limited spending money**. Select details that matter to the named reader.','Reader-focused detail')
q(2,'Choose a sign-off for a formal letter beginning “Dear Ms Patel”, and explain why it fits.','Yours sincerely.\n\nThis suits a formal letter addressed to a **named recipient**.','Letter conventions')
q(2,'Explain the difference between a list of techniques and an effective persuasive argument.','- An argument needs **relevant reasons, supporting detail and explanation**.\n- Techniques help express those ideas; simply including several devices does not make unsupported claims convincing.','Persuasion')
q(4,'Develop “The school library should stay open at lunchtime” into a convincing paragraph for students.','“The library should stay open at lunchtime because not every student has a quiet place to work. Someone sharing a busy home with younger siblings might use that half-hour to finish a difficult task or ask a librarian for help. Keeping the room available would offer a practical choice: students could still meet friends outside, but those who need quiet would have somewhere to go.”\n\n- Clear **claim and reason**.\n- Specific **example**.\n- Explains the **benefit**.\n- Connects the proposal to **students\' different needs**.','Developed paragraph')
q(4,'Plan four distinct paragraph jobs for an article encouraging students to read beyond their set texts.','- **Opening:** recognise that reading can feel like another homework task, then propose reading by choice.\n- **Develop a benefit:** explore a personal interest through a specific example, such as a mystery or sporting biography.\n- **Handle a barrier:** explain how to find an accessible book or try a short sample when time or confidence is limited.\n- **Ending:** recommend one achievable first step, such as asking for a suggestion and trying the opening chapter.','Organisation')
q(4,'Write a concession and response to “A school trip costs too much”, while supporting an affordable trip.','“Some families would find the suggested cost difficult, so we should not dismiss that concern. A local visit with a clear spending limit could offer a useful experience without the price of an overnight stay. The school should explain any available support privately and early, so that cost does not become an embarrassing last-minute surprise.”\n\nThe response **accepts a real concern**, offers a **specific alternative**, explains its **benefit** and keeps a **sensitive tone**.','Counterargument')
q(4,'Improve this review: “The game was good. It was really good and everyone will love it.” Include detail, judgement and a suitable audience.','“The game explains its rules through a short practice round, so new players can join without reading a long instruction booklet. Its ten-minute rounds also suit families who want a quick game between other activities. Experienced players may find the choices rather simple, but beginners looking for an easy introduction should enjoy it.”\n\nIt uses **specific features**, explains their **effects**, recognises a **limitation** and recommends for a **particular audience**.','Review')
q(6,'Rewrite this opening for a school-magazine advice article, then explain three improvements: “EVERYONE is terrible at managing homework!!! Are you lazy? Do you care? You must fix this now.”','“A busy homework week can feel like five people asking for your attention at once. Start by writing down what is due and when, then choose one manageable first task. A clear starting point will not remove the work, but it can make the evening easier to organise.”\n\n- Replaces **accusations** with a situation students can recognise.\n- Gives a **practical action** instead of a string of unanswered questions.\n- Uses **controlled punctuation and a realistic claim**, creating a helpful rather than hostile voice.','Advice, development and control')
q(6,'Edit this paragraph, then explain three changes: “Our school need a reading club, its a brilliant thing. People will enjoy it because it is enjoyable. Their should be one immediately.”','“Our school needs a reading club where students can discuss books they have chosen themselves. A small group could begin by sharing a favourite scene or recommending a character worth following. That would give quieter readers a clear starting point for conversation. A lunchtime trial would let students test the idea before making a weekly commitment.”\n\n- Corrects **agreement** and removes the inaccurate “its” and “Their” constructions.\n- Replaces **repetition** with specific activities and an explanation of their value.\n- Ends with a **practical proposal** rather than an unsupported demand.','Editing')

MODELS=[
('Write an article for your school magazine arguing that the school library should remain open at lunchtime.',
'''A quiet room is not an empty room

At lunchtime, the loudest places in school are easy to find. The harder question is where to go when you need a little quiet. Keeping the library open would give students that choice, and it deserves a place in any discussion about how we use our school day.

For some students, lunchtime is their best chance to work without interruption. At home, a kitchen table may also be a dinner table, a play area and the place where everyone leaves their bags. A short period in the library could allow a student to finish a difficult paragraph or check a reference before the next lesson. That is a modest benefit, but a useful one: the school would be making space for different circumstances rather than assuming everyone has a desk waiting at home.

The library is also a place to discover something that has not been set for homework. A display of short stories, a shelf of biographies or a recommendation from another student can offer an easy starting point. Reading by choice feels different from racing to complete an assignment. Even a few pages might introduce a writer or subject that someone would otherwise never meet.

Of course, keeping a room open requires supervision. It would be unreasonable to demand that staff give up their break without a workable arrangement. That is why we should discuss a limited trial: perhaps selected lunchtimes, a clear capacity limit and agreed rules about noise and food. Students could give feedback, and staff could decide whether the arrangement is manageable before extending it.

This is not a proposal to turn every lunch break into another lesson. Students should still be free to talk, play and rest. It is a proposal to keep one useful option available for those who need it. When we look around a quiet library, we should not see a room doing nothing. We should see a school making room for everyone.''',
['The opening identifies a student need and a clear position.','The middle develops two different benefits with concrete examples.','The staffing paragraph acknowledges a real obstacle and proposes a trial.','The ending returns to the quiet-room image and clarifies the purpose.']),
('Write a helpful article for a school magazine advising students how to make the most of a school trip.',
'''A school trip worth remembering

A school trip begins before you climb onto the coach. A little preparation can make the difference between spending the day searching for your group and actually enjoying the place you have travelled to see. You do not need a complicated plan; you need a few sensible decisions.

First, read the information you have been given. Check the departure time, what to bring and whether food is provided. Put any necessary items together the evening before, rather than trying to find everything while someone is calling you from the front door. If an instruction is unclear, ask a teacher in advance. Guessing is a poor substitute for a quick question.

Next, find one thing you are curious about. If the trip is to a museum, look for an object or period you would like to understand. If it is to a theatre, find out the basic setting of the play without hunting down every plot detail. Having a small question in mind gives you something to notice when you arrive. It also makes the visit feel more personal than simply moving from room to room because the group is moving.

During the day, pay attention to meeting places and instructions. That may sound obvious until two galleries look almost identical and your friends have disappeared into a crowd. Stay with the people you have been asked to stay with, and ask a member of staff if you are unsure. Looking after these practical details leaves more attention free for the experience itself.

Finally, resist the urge to record every moment through a screen. Where photography is allowed, choose a few useful pictures, then spend some time looking properly. Afterwards, write down one surprising thing you learned or one moment you would like to discuss. Your best memory may not be the photograph with everyone in it. It may be the question, performance or unexpected discovery that made the journey worthwhile.''',
['The opening promises useful guidance rather than scolding readers.','The sequence moves from preparation to the visit and then reflection.','Each piece of advice includes how to do it and why it helps.','The ending returns to the idea of a worthwhile experience.']),
('Your school is considering making every student attend an after-school club. Write a letter to the headteacher giving your views and proposing a workable approach.',
'''Dear Ms Patel,

I am writing about the suggestion that every student should attend an after-school club. I support the aim of helping more students discover activities they enjoy. However, I believe compulsory attendance could create difficulties that a more flexible approach would avoid.

Clubs can offer valuable experiences. A student who is reluctant to speak in a large class might contribute confidently to a small debating group. Someone who has never tried coding could discover an interest that changes their subject choices. These opportunities deserve encouragement, and I understand why the school wants them to reach students who might not volunteer immediately.

The difficulty is that staying after school is not equally straightforward for everyone. Some students depend on a particular bus; others have responsibilities at home or activities arranged outside school. Requiring them to attend would not simply change how they spend a spare hour. It could affect other people and arrangements that they cannot control. Students should not have to describe private family circumstances publicly to explain why a compulsory activity is difficult.

A programme of taster sessions would provide a better starting point. Each club could offer a short introduction, with some sessions at lunchtime where staffing allows. Students could ask questions, try a small activity and find out what regular attendance involves. An accessible list could explain timings, any costs and whom to contact. That would make joining easier without assuming that a single timetable suits everybody.

The school could then ask students which sessions interested them and what prevented others from taking part. This would provide useful information for planning future clubs, rather than treating an absence as a lack of enthusiasm. A trial would also give organisers an opportunity to check what they can realistically offer.

Please consider encouraging every student to explore the options while allowing flexibility over attendance. The strongest clubs will be those students can join with interest and confidence, not those they enter worrying about the journey home.

Yours sincerely,
A student''',
['The purpose is clear immediately, with a respectful disagreement.','The letter recognises benefits before explaining practical difficulties.','The alternative is detailed and within the headteacher’s influence.','Greeting, sign-off and register suit a named formal recipient.']),
('Write a talk to your class encouraging students to give something unfamiliar a fair try.',
'''Good morning, everyone.

When did you last decide that you were bad at something before you had even tried it? I have done it. I have looked at a complicated board game, listened to the first thirty seconds of the explanation and quietly decided that watching would be easier. It is a comfortable decision. It is not always a fair one.

We often compare our first attempt with somebody else’s hundredth. The person who solves the puzzle quickly may have spent weeks learning its patterns. The musician who seems completely relaxed may remember an early lesson in which every note went wrong. What looks like a talent from the outside can include a great deal of patient, ordinary practice. We do not see that practice when we arrive halfway through the story.

This does not mean we must enjoy everything. Giving something a fair try is different from promising to do it forever. It means allowing ourselves enough time to understand the activity before passing judgement. Ask a question. Try a small part. Notice one thing that becomes easier on the second attempt. Those are manageable steps, even when the whole activity still looks difficult.

There is another part to this: the way we treat other beginners. If we laugh every time someone gets a rule wrong, we should not be surprised when they stop joining in. A useful explanation or an invitation to practise together can change the atmosphere of a room. We all benefit when making a first attempt feels ordinary rather than embarrassing.

So my suggestion is small. This week, choose one unfamiliar thing that genuinely interests you. Find out how to begin, give it a sensible amount of attention and make your judgement afterwards. You may decide to leave it there, and that is fine. But let the decision come from experience, not from the fear of looking inexperienced.

The next time you catch yourself saying, “I cannot do that,” try adding one word: “yet.” Thank you.''',
['A brief personal example connects with classmates and leads into the point.','The comparison between first and hundredth attempts gives the argument a clear idea.','Direct address and short sentences suit listening as well as reading.','The ending offers a realistic challenge and a memorable final phrase.']),
('Write a review of a game you would recommend to teenagers. Include enough detail to help readers decide whether it suits them.',
'''Harbour Hunt: a small game with a useful twist

Harbour Hunt looks simple when you open the box: a folded town map, a stack of clue cards and four coloured counters. After one round, however, it becomes clear that the game is less about moving quickly than about deciding which information to trust. For teenagers who enjoy puzzles without wanting an evening of complicated rules, that is an appealing combination.

Players work in teams to locate a missing parcel somewhere in the harbour town. Each clue narrows the possibilities, but taking an extra clue costs time. This creates a genuine choice. Do you make a confident guess now, or spend another turn checking whether the description really points to the lighthouse? The best moments come when teammates disagree and have to explain their reasoning. Even a wrong answer can lead to an entertaining argument about the detail everyone missed.

The introductory round is particularly useful. It teaches the main rules through play, so one person does not have to read a booklet aloud while everyone else waits. The map is clearly labelled, and the short clue cards make it easy to return to an earlier detail. A first game can therefore feel like playing rather than preparing to play.

There are limitations. Once you have used a clue set, remembering the answer reduces the challenge of repeating it. Players who want a game they can replay endlessly may find the selection too limited. The pace also depends on the group: someone who insists on solving every clue alone can make the team element frustrating. Agreeing to let everyone explain an idea helps, but the rules cannot create cooperation by themselves.

I would recommend Harbour Hunt for a small group that enjoys discussing possibilities and is happy to take turns. It is less suitable for someone seeking fast reactions or constant action. Choose it for a rainy afternoon with friends who like asking “What if?”, and the quiet-looking box can produce a surprisingly lively table.''',
['The opening identifies the game and the kind of reader it may suit.','Rules are described only where they support an evaluation of the experience.','Specific strengths and limitations make the judgement balanced and useful.','The recommendation names a suitable audience rather than claiming everyone will love it.'])]
for prompt,model,why in MODELS:
 q(20,prompt,model+'\n\n---\n\n**Why this works:**\n\n'+'\n'.join('- '+s for s in why),'Complete original writing model; assessed holistically using AO5/AO6')

def build():
 lines=['# Transactional and persuasive writing questions & answers'];last=None
 for i,item in enumerate(ITEMS,1):
  if item['marks']!=last:last=item['marks'];lines.append(f'## {last} '+('mark' if last==1 else 'marks'))
  lines += [f'**{i}.** '+item['prompt'],'**Answer:**'+('\n\n' if '\n' in item['answer'] or item['answer'].startswith('- ') else ' ')+item['answer']]
  item['number']=i
 lines += ['## Past-paper sources','The short 1–6 mark tasks are original skill-building exercises, not the format of Section B. The five full writing tasks use the 20-mark format; their original model responses illustrate possible approaches, with commentary. The game in the review is fictional.','### Resource directory','- [Eduqas qualification and resources](https://www.eduqas.co.uk/ed/qualifications/english-language-gcse/)\n- [Eduqas Online Exam Review](https://oer.eduqas.co.uk/)\n- [Revision World paper archive](https://revisionworld.com/a2-level-level-revision/english-language-gcse-level/english-language-gcse-past-papers/eduqas-gcse-english-language-past-papers)','### Papers reviewed']
 for y in ['23','24']:
  base='../../00 - Past papers/Component 2/Eduqas-C700U20-1-'
  lines.append(f'- June 20{y}: [question paper]({base}QP-JUN{y}.pdf) · [mark scheme]({base}MS-JUN{y}.pdf). Section B, questions 2.1 and 2.2.')
 lines += ['### How the sample informs this practice','The 2023 paper includes a school-magazine article and a letter giving views; the 2024 paper includes a class talk and a school-magazine advice article. Articles occur in both papers in this two-paper sample, with different purposes. This does not predict a future form or topic. The practice develops transferable writing decisions rather than reproducing those tasks. Review practice broadens coverage of forms named in the specification.','Each full task is assessed through communication and organisation (12 marks) and vocabulary, sentences, spelling and punctuation (8 marks). The commentary explains choices; it is not a point-by-point official mark scheme.']
 (TOPIC/'Questions and Answers').mkdir(exist_ok=True)
 (TOPIC/'Questions and Answers'/(TITLE+' - Questions and Answers.md')).write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
 (TOPIC/'qa-evidence.json').write_text(json.dumps({'reviewed':'2026-10-11','sample':['2023 Component 2 Section B 2.1–2.2','2024 Component 2 Section B 2.1–2.2'],'questions':ITEMS,'model_word_counts':[len(re.findall(r"\b[\w’'-]+\b",m)) for _,m,_ in MODELS]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(len(ITEMS),'questions; model word counts:',[len(re.findall(r"\b[\w’'-]+\b",m)) for _,m,_ in MODELS])
if __name__=='__main__':build()
