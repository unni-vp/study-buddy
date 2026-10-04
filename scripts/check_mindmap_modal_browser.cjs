const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('url');const path=require('path');const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const topic=pathToFileURL(path.resolve('Biology - AQA/01 - Cell biology/index.html')).href;
 const index=pathToFileURL(path.resolve('library/resources/biology-aqa-cell-biology-mind-maps.html')).href;
 const dialog=page.locator('#mindmap-dialog');
 const image=page.locator('#mindmap-full-image');
 const close=()=>page.getByRole('button',{name:'Close mind map',exact:true});
 const names=['Cell biology overview','Cells','Cell processes','Transport processes','Exchange surfaces','Microscopy','Culturing microorganisms'];
 async function loaded(){await page.waitForFunction(()=>{const i=document.getElementById('mindmap-full-image');return i.complete&&i.naturalWidth===2400&&i.getBoundingClientRect().width>0;});}
 async function fullScreen(){
  if(!await dialog.evaluate(d=>d.open))throw Error('Modal did not open');
  const box=await dialog.boundingBox();
  const vp=page.viewportSize();if(box.x!==0||box.y!==0||Math.abs(box.width-vp.width)>1||Math.abs(box.height-vp.height)>1)throw Error('Modal does not cover viewport');
  if(!await page.evaluate(()=>document.body.classList.contains('mindmap-is-open')&&getComputedStyle(document.body).overflow==='hidden'))throw Error('Background can scroll');
 }
 async function fitted(){
  const fits=await image.evaluate(img=>{const a=img.getBoundingClientRect(),b=img.closest('.mindmap-canvas').getBoundingClientRect();return a.width>0&&a.left>=b.left-1&&a.right<=b.right+1&&a.top>=b.top-1&&a.bottom<=b.bottom+1;});
  if(!fits)throw Error('Fit clips the map');
 }
 await page.goto(topic);
 const button=page.getByRole('link',{name:'Mind maps',exact:true});await button.click();await fullScreen();
 if(page.url()!==topic||await dialog.locator('.mindmap-card').count()!==7)throw Error('Topic button should open seven-map modal gallery on the same page');
 await page.screenshot({path:'tmp/mindmap-modal-gallery.png'});
 for(const name of names){
  await dialog.getByRole('button',{name,exact:true}).click();await loaded();await fullScreen();await fitted();
  if(await page.locator('#mindmap-dialog-title').textContent()!==name)throw Error('Wrong map title');
  if(!(await image.getAttribute('src')).endsWith('.svg'))throw Error('Viewer should use the sharp SVG');
  if(name==='Cell biology overview')await page.screenshot({path:'tmp/mindmap-modal-overview.png'});
  if(name==='Cell processes')await page.screenshot({path:'tmp/mindmap-modal-processes.png'});
  await dialog.getByRole('button',{name:'← All maps',exact:true}).click();
 }
 await dialog.getByRole('button',{name:'Transport processes',exact:true}).click();await loaded();
 const before=await image.evaluate(i=>i.getBoundingClientRect().width);
 await dialog.getByRole('button',{name:'Zoom in',exact:true}).click();
 if(await image.evaluate(i=>i.getBoundingClientRect().width)<=before)throw Error('Zoom in failed');
 await dialog.getByRole('button',{name:'100%',exact:true}).click();
 if(Math.abs(await image.evaluate(i=>i.getBoundingClientRect().width)-2400)>1)throw Error('Actual size failed');
 const canvas=dialog.locator('.mindmap-canvas');
 await canvas.evaluate(n=>{n.scrollLeft=400;n.scrollTop=300;});
 const box=await canvas.boundingBox();const start=await canvas.evaluate(n=>n.scrollLeft);
 await page.mouse.move(box.x+400,box.y+350);await page.mouse.down();await page.mouse.move(box.x+300,box.y+300);await page.mouse.up();
 if(await canvas.evaluate(n=>n.scrollLeft)<=start)throw Error('Mouse panning failed');
 await page.screenshot({path:'tmp/mindmap-modal-zoom.png'});
 await dialog.getByRole('button',{name:'Fit',exact:true}).click();await fitted();
 // Keyboard focus stays inside the native modal.
 for(let i=0;i<14;i++){await page.keyboard.press('Tab');if(!await page.evaluate(()=>document.getElementById('mindmap-dialog').contains(document.activeElement)))throw Error('Focus escaped the dialog');}
 await page.keyboard.press('Escape');
 if(await dialog.evaluate(d=>d.open)||!await button.evaluate(n=>n===document.activeElement)||await page.evaluate(()=>document.body.classList.contains('mindmap-is-open')))throw Error('Escape did not close/restore focus and scrolling');
 // The original thumbnail gallery still works with ordinary-link fallbacks.
 await page.goto(index);const card=page.locator('main .mindmap-card').filter({hasText:'Cells'});await card.click();await loaded();await fullScreen();
 await close().click();if(!await card.evaluate(n=>n===document.activeElement))throw Error('Close did not restore thumbnail focus');
 // Direct-reader bookmarks have an accessible text version and full-screen button.
 await page.goto(index.replace('-mind-maps.html','-01-cells.html'));await page.getByRole('button',{name:'Open full screen',exact:true}).click();await loaded();
 await dialog.getByRole('link',{name:'Text version',exact:true}).click();
 if(await dialog.evaluate(d=>d.open)||!await page.locator('#text-version').evaluate(n=>n.open)||!await page.getByRole('heading',{name:'Root hair cells',exact:true}).isVisible())throw Error('Text version did not reveal all content');
 // Printing a zoomed map prints the map alone, without controls or site navigation.
 await page.getByRole('button',{name:'Open full screen',exact:true}).click();await loaded();await dialog.getByRole('button',{name:'100%',exact:true}).click();
 await page.emulateMedia({media:'print'});
 if(await dialog.locator('.mindmap-toolbar').isVisible()||await page.locator('.layout').isVisible()||!await image.isVisible())throw Error('Print shows controls/background or hides the map');
 await page.emulateMedia({media:'screen'});await close().click();
 // Narrow screens retain full-screen fitting and readable 100% zoom with touch scrolling.
 await page.setViewportSize({width:390,height:844});await page.goto(topic);await page.getByRole('link',{name:'Mind maps',exact:true}).click();await fullScreen();
 await dialog.getByRole('button',{name:'Culturing microorganisms',exact:true}).click();await loaded();await fitted();
 await page.screenshot({path:'tmp/mindmap-modal-mobile-fit.png'});
 await dialog.getByRole('button',{name:'100%',exact:true}).click();
 if(await canvas.evaluate(n=>n.scrollWidth<=n.clientWidth)||await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Mobile zoom cannot scroll or makes the page overflow');
 await canvas.evaluate(n=>{n.scrollLeft=0;n.scrollTop=0;});await page.screenshot({path:'tmp/mindmap-modal-mobile-zoom.png'});
 await close().click();
 // Standalone resource HTML uses the same viewer.
 await page.goto(pathToFileURL(path.resolve('Biology - AQA/01 - Cell biology/Mind Maps/Cell Biology - Mind Maps.html')).href);
 await page.locator('main .mindmap-card').filter({hasText:'Microscopy'}).click();await loaded();await fullScreen();await close().click();
 // No JavaScript: thumbnail links open their complete map readers.
 const nojs=await browser.newContext({javaScriptEnabled:false});const plain=await nojs.newPage();await plain.goto(index);
 await plain.getByRole('link',{name:'Cells',exact:true}).click();
 if(await plain.locator('figure img').count()!==1)throw Error('No-script fallback failed');
 await plain.locator('details.mindmap-text > summary').click();if(!await plain.getByRole('heading',{name:'Animal cells',exact:true}).isVisible())throw Error('No-script text content missing');
 await nojs.close();
 // Verify relative assets with the same /study-buddy/ prefix as GitHub Pages.
 const http=require('http');const root=path.resolve('.');
 const server=http.createServer((req,res)=>{
  const url=new URL(req.url,'http://127.0.0.1');
  const relative=decodeURIComponent(url.pathname.replace(/^\/study-buddy\//,''));
  const file=path.resolve(root,relative);
  if(!file.startsWith(root+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404);res.end();return;}
  const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png'};
  res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');res.end(fs.readFileSync(file));
 });
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const hosted=await browser.newPage();const hostedErrors=[];hosted.on('pageerror',e=>hostedErrors.push(e.message));
 await hosted.goto('http://127.0.0.1:'+server.address().port+'/study-buddy/Biology%20-%20AQA/01%20-%20Cell%20biology/index.html');
 await hosted.getByRole('link',{name:'Mind maps',exact:true}).click();
 await hosted.locator('#mindmap-dialog').getByRole('button',{name:'Microscopy',exact:true}).click();
 await hosted.waitForFunction(()=>document.getElementById('mindmap-full-image').naturalWidth===2400);
 if(hostedErrors.length)throw Error(hostedErrors.join(';'));
 await hosted.close();await new Promise(resolve=>server.close(resolve));
 if(errors.length)throw Error(errors.join(';'));
 await browser.close();console.log('PASS: seven full-screen SVG maps, topic/gallery/direct/standalone entry, fit/zoom/pan, keyboard focus and Escape, background locking, print isolation, mobile scrolling no-script text fallbacks and hosted /study-buddy/ asset paths.');
})().catch(e=>{console.error(e);process.exit(1)});
