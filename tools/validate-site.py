"""Static integrity checks for both language pages and generated metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.nodes=[]; self.ids=[]; self.schema=''; self.in_schema=False; self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs); self.nodes.append((tag,a))
  if 'id' in a: self.ids.append(a['id'])
  if tag=='h1': self.h1+=1
  if tag=='script' and a.get('type')=='application/ld+json': self.in_schema=True
 def handle_endtag(self,tag):
  if tag=='script': self.in_schema=False
 def handle_data(self,data):
  if self.in_schema: self.schema+=data

count=0
for filename,language in [('index.html','es-UY'),('pt/index.html','pt-BR')]:
 path=ROOT/filename; page=Page(); page.feed(path.read_text(encoding='utf-8'))
 assert page.h1==1, filename+' needs one h1'
 assert len(page.ids)==len(set(page.ids)), 'Duplicate IDs'
 assert next(a for t,a in page.nodes if t=='html')['lang']==language
 for tag,a in page.nodes:
  if tag=='img': assert all(k in a for k in ['alt','width','height']), a
  for key in ['href','src','data-src']:
   value=a.get(key,''); target=urlsplit(value)
   if not value or target.scheme or target.netloc: continue
   if target.path:
    local=(path.parent/unquote(target.path)).resolve()
    assert local.exists(), f'{filename}: missing {value}'
   elif target.fragment: assert target.fragment in page.ids, f'Broken anchor {value}'
   count+=1
  for key in ['srcset','data-srcset']:
   for candidate in a.get(key,'').split(','):
    if candidate.strip(): assert (path.parent/candidate.strip().split()[0]).exists(), candidate
 data=json.loads(page.schema)
 graph=data['@graph']; business=next(x for x in graph if x['@type']=='AutoRepair')
 assert business['telephone']=='+59898738689'
 assert business['address']['streetAddress']=='Paysandú 255'
 assert 'aggregateRating' not in business
 assert any('BAIA' in offer['itemOffered']['name'] for offer in business['hasOfferCatalog']['itemListElement'])
 assert len([a for t,a in page.nodes if t=='a' and a.get('class')=='gallery-link'])==4
 assert 'Unsplash' not in path.read_text(encoding='utf-8')
 assert len(next(x for x in graph if x['@type']=='FAQPage')['mainEntity'])==6
 links=[a for t,a in page.nodes if t=='link']
 assert len([a for a in links if a.get('rel')=='canonical'])==1
 assert set(a['hreflang'] for a in links if 'hreflang' in a)=={'es-UY','pt-BR','x-default'}
 assert '<iframe' not in path.read_text(encoding='utf-8'), 'Map should be interaction-loaded'
 print(filename, 'PASS: structure, assets, anchors, locales and schema')
sitemap=ET.parse(ROOT/'sitemap.xml')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'}
base='https://dfchanel-coder.github.io/topcarrivera/'
urls=sitemap.findall('s:url',ns)
assert {u.find('s:loc',ns).text for u in urls}=={base,base+'pt/'}
for url in urls:
 assert {x.get('hreflang'):x.get('href') for x in url.findall('x:link',ns)}=={'es-UY':base,'pt-BR':base+'pt/','x-default':base}
 assert url.find('s:lastmod',ns).text=='2026-11-02'
 images=url.findall('{http://www.google.com/schemas/sitemap-image/1.1}image')
 assert len(images)==6
 for image in images:
  location=image.find('{http://www.google.com/schemas/sitemap-image/1.1}loc').text
  assert location.startswith(base)
  assert (ROOT/location.removeprefix(base)).exists()
robots=(ROOT/'robots.txt').read_text(encoding='utf-8')
assert f'Sitemap: {base}sitemap.xml' in robots
assert 'User-agent: *\nAllow: /' in robots
assert 'Disallow:' not in robots
json.loads((ROOT/'site.webmanifest').read_text(encoding='utf-8'))
print(f'PASS: {count} local references, sitemap XML and webmanifest JSON')
