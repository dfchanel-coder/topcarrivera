import {spawnSync} from 'node:child_process';
import {readFileSync, writeFileSync, mkdirSync, existsSync} from 'node:fs';
import {resolve} from 'node:path';
const root = resolve(import.meta.dirname, '..');
const chrome = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
if (!existsSync(chrome)) throw new Error('Set CHROME_PATH to your Chrome executable.');
mkdirSync(resolve(root,'.cache'),{recursive:true});
const summary=[];
for (const locale of ['es','pt']) for (const form of ['mobile','desktop']) {
  const output=resolve(root,`.cache/lighthouse-${locale}-${form}`);
  const args=[resolve(root,'node_modules/lighthouse/cli/index.js'),`http://127.0.0.1:8123/topcarrivera/${locale==='pt'?'pt/':''}`,`--chrome-path=${chrome}`,'--chrome-flags=--headless --disable-gpu','--output=json','--output=html',`--output-path=${output}`,'--quiet'];
  if(form==='desktop')args.push('--preset=desktop');
  const run=spawnSync(process.execPath,args,{cwd:root,stdio:'inherit',windowsHide:true});
  if(run.status!==0)throw new Error(`Lighthouse failed: ${locale}/${form}`);
  const report=JSON.parse(readFileSync(output+'.report.json','utf8'));
  const scores=Object.fromEntries(Object.entries(report.categories).map(([key,value])=>[key,Math.round(value.score*100)]));
  const result={locale,form,scores,LCP:report.audits['largest-contentful-paint'].displayValue,CLS:report.audits['cumulative-layout-shift'].displayValue,TBT:report.audits['total-blocking-time'].displayValue};
  summary.push(result);
  console.log(JSON.stringify(result));
  writeFileSync(resolve(root,'.cache/audit-summary.json'),JSON.stringify(summary,null,2));
  if(Object.values(scores).some(score=>score<=90))process.exitCode=1;
}
