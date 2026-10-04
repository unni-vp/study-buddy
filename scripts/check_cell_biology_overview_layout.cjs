// Preserve the existing overview-check entry point; use transform-aware checks.
const {spawnSync}=require('child_process');
const result=spawnSync(process.execPath,['scripts/check_landscape_mindmaps.cjs','00-cell-biology-overview.svg'],{stdio:'inherit'});
if(result.error)throw result.error;
process.exitCode=result.status??1;
