const { chromium } = require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('url');
const path = require('path');

(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(path.resolve('Biology - AQA/01 - Cell biology/index.html')).href);
 await page.getByRole('link',{name:'Questions & answers',exact:true}).click();
 const index=page.url();
 const expectedTitles=['1 mark','2 marks','3 marks','4 marks','5 marks','6 marks'];
 async function checkBank(){
  if(await page.locator('.revision-group, .section-choice, .section-navigation').count())throw Error('Unwanted Q&A split or menu');
  const titles=await page.locator('.reading h2').allTextContents();
  if(JSON.stringify(titles)!==JSON.stringify(expectedTitles))throw Error('Only the six mark headings should be displayed');
  if(await page.locator('.reading h3, .reading h4, .reading h5, .reading h6').count())throw Error('Individual question/answer headings remain');
  const pairs=await page.locator('.qa-question').evaluateAll(nodes=>nodes.map(n=>({
   id:n.id,number:Number(n.querySelector('p strong').textContent.replace('.','')),
   prompt:n.querySelector('p').textContent,
   answer:[...n.querySelectorAll('p')].some(p=>p.textContent.startsWith('Answer:')&&(p.textContent.slice(7).trim()||p.nextElementSibling?.textContent.trim()||n.querySelector('ul li')))
  })));
  if(pairs.length!==42||pairs.some((q,i)=>q.number!==i+1||q.id!==`q${String(i+1).padStart(2,'0')}`||!q.answer))throw Error('Incomplete or misnumbered Q&A pairs');
  if(await page.getByText('Answer — suggested marking points',{exact:true}).count())throw Error('Old answer label remains');
  for(const id of ['q03','q04']){
   const answer=page.locator('#'+id+' p').filter({hasText:'Answer:'});
   if(await answer.locator('strong').count()!==1||await answer.locator('strong').textContent()!=='Answer:')throw Error('Short answer should be plain text');
  }
  if(pairs.some(q=>/\(\d+ marks?\)/.test(q.prompt)))throw Error('Repeated marks on individual questions');
  const counts=await page.locator('.qa-mark-group').evaluateAll(groups=>groups.map(g=>g.querySelectorAll('.qa-question').length));
  if(JSON.stringify(counts)!==JSON.stringify([10,8,11,4,3,6]))throw Error('Question moved to the wrong mark group');
  if(await page.locator('.reading img').count()!==3||!await page.locator('.reading img').evaluateAll(imgs=>imgs.every(i=>i.complete&&i.naturalWidth>0)))throw Error('Question diagrams missing');
  if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Horizontal overflow');
 }
 await checkBank();
 await page.screenshot({path:'tmp/qa-index.png',fullPage:false});
 for(const [i,title] of expectedTitles.entries()){
  await page.getByRole('link',{name:title,exact:true}).click();
  if(page.url().split('#')[0]!==index||!page.url().endsWith(`#marks-${i+1}`))throw Error('Mark link opens another page');
  const top=await page.locator(`#marks-${i+1}`).evaluate(n=>n.getBoundingClientRect().top);
  if(top<0||top>100)throw Error('Mark link does not reach its section');
 }
 await page.setViewportSize({width:390,height:844});
 await page.goto(index);await checkBank();
 await page.screenshot({path:'tmp/qa-index-mobile.png',fullPage:false});
 await page.getByRole('link',{name:'4 marks',exact:true}).click();
 await page.screenshot({path:'tmp/qa-four-marks-mobile.png',fullPage:false});
 await page.goto(index);
 await page.getByRole('link',{name:'Past-paper sources',exact:true}).click();
 if(await page.locator('.reading a[href$=".pdf"]').count()!==12)throw Error('Source papers or mark schemes missing');
 if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Sources mobile overflow');
 await page.goto(index.replace('.html','-all.html'));await checkBank();
 await page.getByRole('button',{name:'Print all Q&A',exact:true}).waitFor();
 await page.emulateMedia({media:'print'});
 if(await page.locator('.qa-mark-links').isVisible())throw Error('Jump links should be hidden when printing');
 if(await page.locator('.qa-question:visible').count()!==42)throw Error('Printing hides questions');
 if(errors.length)throw Error(errors.join(';'));
 console.log('PASS: one combined topic page; 42 complete numbered Q&A pairs in six mark groups; no individual headings or mark labels; same-page jump links; 3 loaded diagrams; 12 source PDFs; print and desktop/mobile checks.');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
