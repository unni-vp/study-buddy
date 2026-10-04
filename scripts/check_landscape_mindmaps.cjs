// Real browser font metrics, transformed section bounds and full-canvas containment.
const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try {
  const page=await browser.newPage({viewport:{width:2400,height:2000}});
  const dir='Biology - AQA/01 - Cell biology/Mind Maps';
  const files=process.argv.slice(2);if(!files.length)files.push(...fs.readdirSync(dir).filter(f=>f.endsWith('.svg')));
  for(const file of files){
   await page.setContent('<!doctype html><style>body{margin:0}</style>'+fs.readFileSync(path.join(dir,file),'utf8'));
   await page.evaluate(()=>document.fonts.ready);
   const result=await page.evaluate(()=>{
    const outside=[],overlaps=[],crowding=[],pathCollisions=[];const canvas=document.querySelector('body>svg').getBoundingClientRect();
    const nodes=[...document.querySelectorAll('svg text')].map(el=>{const b=el.getBoundingClientRect();return {el,text:el.textContent,x:b.x,y:b.y,r:b.right,b:b.bottom,section:el.closest('.map-section')?.id||'relationships'};});
    for(const a of nodes){
     if(a.x < -1||a.r>canvas.right+1||a.y < -1||a.b>canvas.bottom+1)outside.push({section:'canvas',text:a.text});
     const sec=a.el.closest('.map-section');
     if(sec){
      const [x,y,w,h]=sec.dataset.bounds.split(',').map(Number);const matrix=sec.getScreenCTM();
      const p=new DOMPoint(x,y).matrixTransform(matrix),q=new DOMPoint(x+w,y+h).matrixTransform(matrix);
      if(a.x<p.x-1||a.r>q.x+1||a.y<p.y-1||a.b>q.y+1)outside.push({section:a.section,text:a.text});
     }
    }
    for(let i=0;i<nodes.length;i++)for(let j=i+1;j<nodes.length;j++){
     const a=nodes[i],b=nodes[j],dx=Math.min(a.r,b.r)-Math.max(a.x,b.x),dy=Math.min(a.b,b.b)-Math.max(a.y,b.y);
     if(dx>1&&dy>1.3)overlaps.push({section:a.section,otherSection:b.section,text:[a.text,b.text],overlap:[+dx.toFixed(2),+dy.toFixed(2)]});
    }
    const panels=[...document.querySelectorAll('.map-section,.map-hub')].map(el=>{
     const [x,y,w,h]=el.dataset.bounds.split(',').map(Number),m=el.getScreenCTM();
     const p=new DOMPoint(x,y).matrixTransform(m),q=new DOMPoint(x+w,y+h).matrixTransform(m);
     return {el,id:el.id||'central heading',x:p.x,y:p.y,r:q.x,b:q.y};
    });
    for(const panel of panels.filter(p=>p.el.matches('.map-section'))){
     const body=panel.el.querySelector('.section-body')?.getBoundingClientRect();
     const head=panel.el.querySelector('.section-heading')?.getBoundingClientRect();
     if(!body||!head){crowding.push([panel.id,'Missing padding metadata']);continue;}
     const margins=[body.left-panel.x,panel.r-body.right,panel.b-body.bottom];
     if(Math.min(...margins)<16)crowding.push([panel.id,'Body inset',margins.map(n=>+n.toFixed(1))]);
     if(body.top-head.bottom<18)crowding.push([panel.id,'Heading/body gap',+(body.top-head.bottom).toFixed(1)]);
    }
    for(let i=0;i<panels.length;i++)for(let j=i+1;j<panels.length;j++){
     const a=panels[i],b=panels[j];
     const gx=Math.max(a.x-b.r,b.x-a.r,0),gy=Math.max(a.y-b.b,b.y-a.b,0);
     if(Math.hypot(gx,gy)<20)crowding.push([a.id,b.id,'Less than 20 px clear space']);
    }
    for(const hub of panels.filter(p=>p.el.matches('.map-hub'))){
     for(const t of nodes.filter(n=>n.el.closest('.map-hub')===hub.el))
      if(t.x<hub.x+18||t.r>hub.r-18||t.y<hub.y+18||t.b>hub.b-18)crowding.push(['Title padding',t.text]);
    }
    for(const p of document.querySelectorAll('.relationship-path')){
     const length=p.getTotalLength(),matrix=p.getScreenCTM();
     for(let k=1;k<600;k++){
      const q=p.getPointAtLength(length*k/600),v=new DOMPoint(q.x,q.y).matrixTransform(matrix);
      const hit=panels.find(b=>v.x>b.x+3&&v.x<b.r-3&&v.y>b.y+3&&v.y<b.b-3);
      if(hit){pathCollisions.push({panel:hit.id,path:p.getAttribute('d')});break;}
     }
    }
    return {texts:nodes.length,ratio:canvas.width/canvas.height,outside,overlaps,crowding,pathCollisions};
   });
   if(result.outside.length||result.overlaps.length||result.ratio<=1||result.crowding.length||result.pathCollisions.length)throw Error(file+'\n'+JSON.stringify(result,null,2));
   console.log(`PASS ${file}: ${result.texts} text elements; landscape; no text/section collisions, cramped gaps, or connectors crossing panels.`);
  }
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
