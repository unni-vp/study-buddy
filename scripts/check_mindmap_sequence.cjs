const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('url');
const path=require('path');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const page=await browser.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  const topic=process.argv[2]||'01 - Cell biology';
  const url=pathToFileURL(path.resolve('Biology - AQA',topic,'index.html')).href;
  for(const width of [1440,390]){
   await page.setViewportSize({width,height:900});await page.goto(url);
   const catalog=JSON.parse(await page.locator('#mindmap-catalog').textContent());
   const trigger=page.getByRole('link',{name:'Mind maps',exact:true});await trigger.click();
   const dialog=page.locator('#mindmap-dialog');
   if(await dialog.locator('.mindmap-sequence').isVisible())throw Error('Sequence visible in gallery');
   await dialog.locator('.mindmap-card').first().click();
   const previous=dialog.getByRole('button',{name:'Previous mind map',exact:true});
   const next=dialog.getByRole('button',{name:'Next mind map',exact:true});
   async function current(index){
    await page.waitForFunction(()=>{const i=document.getElementById('mindmap-full-image');return i.complete&&i.naturalWidth>0&&i.getBoundingClientRect().width>0;});
    if(page.url()!==url||!await dialog.evaluate(d=>d.open))throw Error('Navigation left modal');
    if(await dialog.locator('#mindmap-dialog-title').textContent()!==catalog[index].title)throw Error('Wrong title');
    if(await dialog.locator('#mindmap-position').textContent()!==`${index+1} / ${catalog.length}`)throw Error('Wrong count');
    if(await previous.isDisabled()!==(index===0)||await next.isDisabled()!==(index===catalog.length-1))throw Error('Wrong boundary state');
    const image=dialog.locator('#mindmap-full-image');
    if(!await image.evaluate(i=>{const a=i.getBoundingClientRect(),b=i.closest('.mindmap-canvas').getBoundingClientRect();return a.left>=b.left-1&&a.right<=b.right+1&&a.top>=b.top-1&&a.bottom<=b.bottom+1;}))throw Error('Navigation did not fit new map');
    if((await dialog.locator('#mindmap-text-link').getAttribute('href'))!==catalog[index].page+'#text-version')throw Error('Stale text link');
   }
   await current(0);
   await dialog.getByRole('button',{name:'Zoom in',exact:true}).click();
   for(let i=1;i<catalog.length;i++){await next.click();await current(i);}
   for(let i=catalog.length-2;i>=0;i--){await previous.click();await current(i);}
   await page.keyboard.press('Escape');
   if(!await trigger.evaluate(t=>t===document.activeElement))throw Error('Focus not restored');
  }
  if(errors.length)throw Error(errors.join('\n'));
  console.log('PASS',topic,'Previous/Next, title/count/text updates, boundary states, fit reset and focus on desktop/mobile');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
