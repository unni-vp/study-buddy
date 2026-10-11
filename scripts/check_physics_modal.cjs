const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('url');const path=require('path');
const topics=['01 - Energy','02 - Electricity','03 - Particle model of matter','04 - Atomic structure','05 - Forces'];
const counts=[4,4,3,4,6];
(async()=>{const b=await chromium.launch({channel:'msedge',headless:true});try{
 const p=await b.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
 for(let t=0;t<topics.length;t++)for(const width of [1440,390]){
  await p.setViewportSize({width,height:900});await p.goto(pathToFileURL(path.resolve('Physics - AQA',topics[t],'index.html')).href);
  const trigger=p.getByRole('link',{name:'Mind maps',exact:true});await trigger.click();const d=p.locator('#mindmap-dialog');
  const box=await d.boundingBox();if(box.x!==0||box.y!==0||box.width!==width||box.height!==900)throw Error('Not fullscreen');
  if(await d.locator('.mindmap-card').count()!==counts[t])throw Error('Gallery count');
  for(let i=0;i<counts[t];i++){
   await d.locator('.mindmap-card').nth(i).click();const im=p.locator('#mindmap-full-image');await im.evaluate(i=>i.decode());
   if(!await im.evaluate(i=>{const a=i.getBoundingClientRect(),c=i.closest('.mindmap-canvas').getBoundingClientRect();return a.width>0&&a.left>=c.left-1&&a.right<=c.right+1&&a.bottom<=c.bottom+1}))throw Error('Fit');
   const old=(await im.boundingBox()).width;await d.getByRole('button',{name:'Zoom in',exact:true}).click();if((await im.boundingBox()).width<=old)throw Error('Zoom');
   await d.getByRole('button',{name:'Fit',exact:true}).click();await d.getByRole('button',{name:'← All maps',exact:true}).click();
  }
  await p.keyboard.press('Escape');if(await d.evaluate(n=>n.open)||!await trigger.evaluate(n=>n===document.activeElement))throw Error('Escape/focus');
  if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Overflow');
  console.log('PASS modal',topics[t],width);
 }
 if(errors.length)throw Error(errors.join(';'));
}finally{await b.close()}})().catch(e=>{console.error(e);process.exit(1)});
