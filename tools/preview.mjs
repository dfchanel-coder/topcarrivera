import http from 'node:http';
import {readFile, stat} from 'node:fs/promises';
import {resolve, extname, sep} from 'node:path';
const root = resolve(import.meta.dirname, '..');
const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.woff':'font/woff','.png':'image/png','.jpg':'image/jpeg','.ico':'image/x-icon','.json':'application/json','.webmanifest':'application/manifest+json','.txt':'text/plain; charset=utf-8','.xml':'application/xml'};
http.createServer(async (req,res) => {
  try {
    let pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (pathname === '/topcarrivera') { res.writeHead(301,{Location:'/topcarrivera/'}).end(); return; }
    pathname = pathname.replace(/^\/topcarrivera(?=\/)/,'');
    let path = resolve(root, '.' + pathname);
    if (path !== root && !path.startsWith(root+sep)) { res.writeHead(403).end(); return; }
    if ((await stat(path)).isDirectory()) {
      if (!pathname.endsWith('/')) { res.writeHead(301,{Location:req.url+'/'}).end(); return; }
      path = resolve(path,'index.html');
    }
    const body = await readFile(path);
    res.writeHead(200,{'Content-Type':types[extname(path)] || 'application/octet-stream','Content-Length':body.length,'Cache-Control':'no-cache'});
    res.end(req.method === 'HEAD' ? undefined : body);
  } catch { res.writeHead(404,{'Content-Type':'text/plain'}).end('Not found'); }
}).listen(8123,'127.0.0.1',() => console.log('TOP CAR preview: http://127.0.0.1:8123/topcarrivera/'));
