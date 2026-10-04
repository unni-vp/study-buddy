const { chromium } = require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('url');
const path = require('path');
const fs = require('fs');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(pathToFileURL(path.resolve('index.html')).href);
 if(await page.locator('.subject-card').count()!==9)throw Error('Missing subject cards');
 if(await page.locator('.subject-icon svg').count()!==9)throw Error('Missing subject icons');
 await page.screenshot({path:'tmp/library-home.png',fullPage:true});
 await page.locator('.subject-card').filter({hasText:'Biology'}).click();
 await page.locator('.topic-row').filter({hasText:'Cell biology'}).click();
 if(!await page.getByRole('link',{name:'Questions & answers',exact:true}).isVisible())throw Error('Q&A category missing or disabled');
 if(await page.locator('.resource-button .resource-icon').count()!==3)throw Error('Resource button icons missing');
 await page.screenshot({path:'tmp/library-topic.png',fullPage:true});
 await page.getByRole('link',{name:'Revision notes',exact:true}).click();
 const revisionIndex=page.url();
 const layout=JSON.parse(fs.readFileSync('Biology - AQA/01 - Cell biology/revision-layout.json','utf8'));
 const sections=layout.groups;
 if(await page.locator('.revision-group').count()!==4)throw Error('Four revision groups missing');
 if(await page.locator('.reading').count())throw Error('Revision index still contains the complete notes');
 if(await page.evaluate(()=>document.documentElement.scrollHeight>window.innerHeight))throw Error('Desktop revision index requires scrolling');
 await page.screenshot({path:'tmp/revision-index.png',fullPage:true});
 let diagramCount=0;
 const sectionUrls={};
 for(const group of layout.groups){
  await page.goto(revisionIndex);
  await page.getByRole('link',{name:group.title+' '+group.description,exact:true}).click();
  sectionUrls[group.id]=page.url();
  await page.getByRole('heading',{name:group.title,exact:true}).waitFor();
  if(await page.locator('.section-choice').count())throw Error('Unwanted second-level splits');
  if(await page.locator('.reading h1').count()!==1)throw Error('A group must open one notes document');
  if(!await page.locator('.reading img').evaluateAll(imgs=>imgs.every(i=>i.complete&&i.naturalWidth>0)))throw Error('Broken note diagram');
  diagramCount+=await page.locator('.reading img').count();
  const i=sections.findIndex(s=>s.id===group.id);
  if(await page.locator('.section-navigation a').count()!==((i>0?1:0)+(i<sections.length-1?1:0)))throw Error('Previous/Next links missing');
  if(group.id==='cell-processes')await page.locator('.reading img').screenshot({path:'tmp/mitosis-reader.png'});
  const relatedMaps=await page.locator('.revision-utilities a').filter({hasText:'mind map'}).evaluateAll(a=>a.map(x=>x.href));
  for(const url of relatedMaps){
   await page.goto(url);
   if(await page.locator('.mindmap-view img').count()!==1)throw Error('Related map link failed');
  }
  await page.goto(sectionUrls[group.id]);
  await page.getByRole('link',{name:'← All revision notes',exact:true}).click();
  if(page.url()!==revisionIndex)throw Error('Back to revision menu failed');
 }
 if(diagramCount!==3)throw Error('Note diagrams were lost or duplicated when splitting');
 await page.goto(sectionUrls['cells']);
 for(let i=1;i<sections.length;i++){
  await page.locator('.section-navigation a').filter({hasText:'Next →'}).click();
  if(page.url()!==sectionUrls[sections[i].id])throw Error('Next sequence is incorrect');
 }
 await page.locator('.section-navigation a').filter({hasText:'← Previous'}).click();
 if(page.url()!==sectionUrls[sections.at(-2).id])throw Error('Previous sequence is incorrect');
 await page.goto(revisionIndex);
 for(const extra of layout.extras){
  await page.getByRole('link',{name:extra.title,exact:true}).click();
  await page.getByRole('heading',{name:extra.title,exact:true}).waitFor();
  await page.getByRole('link',{name:'← All revision notes',exact:true}).click();
 }
 await page.getByRole('link',{name:'Print all notes',exact:true}).click();
 await page.getByRole('heading',{name:'9. Required practical 3: osmosis in plant tissue'}).waitFor();
 if(await page.locator('.reading img').count()!==3)throw Error('Print view is incomplete');
 if((await page.locator('.reading').innerText()).includes('AQA GCSE Biology 8461 | Higher tier | Summer 2027'))throw Error('Repeated qualification banner');
 await page.getByRole('button',{name:'Print all notes',exact:true}).waitFor();
 await page.getByRole('link',{name:'← All revision notes',exact:true}).click();
 await page.getByRole('link',{name:'← Back to topic'}).click();
 await page.goto(await page.getByRole('link',{name:'Mind maps',exact:true}).evaluate(a=>a.href));
 if(await page.locator('main .mindmap-card').count()!==7)throw Error('Mind-map buttons missing');
 if(await page.locator('main .mindmap-thumbnail').count()!==7)throw Error('Mind-map thumbnails missing');
 if(!await page.locator('main .mindmap-thumbnail').evaluateAll(imgs=>imgs.every(i=>i.complete&&i.naturalWidth>0)))throw Error('Broken mind-map thumbnail');
 if(!await page.locator('main .mindmap-card').evaluateAll(cards=>cards.slice(0,4).every(c=>Math.abs(c.getBoundingClientRect().top-cards[0].getBoundingClientRect().top)<1)))throw Error('Desktop mind-map cards should fit four across');
 if(await page.locator('figure img').count()!==0)throw Error('Mind-map index still contains a scrolling gallery');
 await page.screenshot({path:'tmp/mindmap-index.png',fullPage:true});
 for(const title of ['Cell biology overview','Cells','Cell processes','Transport processes','Exchange surfaces','Microscopy','Culturing microorganisms']){
  await page.getByRole('link',{name:title,exact:true}).locator('img').click();
  await page.locator('#mindmap-dialog[open]').waitFor();
  await page.waitForFunction(()=>document.getElementById('mindmap-full-image').naturalWidth===2400);
  await page.getByRole('heading',{name:title,exact:true}).waitFor();
  await page.getByRole('button',{name:'Close mind map',exact:true}).click();
 }
 await page.setViewportSize({width:390,height:844});
 await page.goto(pathToFileURL(path.resolve('index.html')).href);
 if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Mobile home overflow');
 await page.screenshot({path:'tmp/library-mobile.png',fullPage:true});
 await page.locator('.subject-card').filter({hasText:'Biology'}).click();
 await page.locator('.topic-row').filter({hasText:'Cell biology'}).click();
 await page.screenshot({path:'tmp/library-topic-mobile.png',fullPage:true});
 await page.getByRole('link',{name:'Revision notes',exact:true}).click();
 if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Mobile revision index overflow');
 await page.screenshot({path:'tmp/revision-index-mobile.png',fullPage:true});
 for(const url of Object.values(sectionUrls)){
  await page.goto(url);
  if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Mobile section overflow: '+url);
 }
 await page.goto(sectionUrls['cell-processes']);
 await page.screenshot({path:'tmp/revision-section-mobile.png',fullPage:true});
 await page.goto(revisionIndex);
 await page.getByRole('link',{name:'← Back to topic'}).click();
 await page.goto(await page.getByRole('link',{name:'Mind maps',exact:true}).evaluate(a=>a.href));
 if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Mobile map index overflow');
 await page.screenshot({path:'tmp/mindmap-index-mobile.png',fullPage:true});
 await page.getByRole('link',{name:'Cells',exact:true}).locator('img').click();
 if(await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth))throw Error('Mobile mind map overflow');
 if(errors.length)throw Error(errors.join('\n'));
 await browser.close();console.log('PASS: four direct revision pages without sub-menus, Previous/Next and related maps, full print notes, mind-map navigation and desktop/mobile layouts.');
})().catch(e=>{console.error(e);process.exit(1)});
