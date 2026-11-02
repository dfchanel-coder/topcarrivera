"""Create responsive WebP copies without modifying supplied originals."""
from pathlib import Path
from PIL import Image, ImageOps
import json

ROOT=Path(__file__).resolve().parent.parent
OUTPUT=ROOT/'assets/photos/real'
SOURCES={
 'taller-en-actividad':'WhatsApp Image 2026-11-02 at 09.13.10 (2).jpeg',
 'frenos':'WhatsApp Image 2026-11-02 at 09.13.14.jpeg',
 'embrague':'WhatsApp Image 2026-11-02 at 09.13.08 (2).jpeg',
 'fachada':'WhatsApp Image 2026-11-02 at 09.13.09.jpeg',
 'interior':'WhatsApp Image 2026-11-02 at 09.13.11.jpeg',
 'auxilio-baia':'WhatsApp Image 2026-11-02 at 09.13.13.jpeg',
}
OUTPUT.mkdir(parents=True,exist_ok=True)
manifest={}
for name,source in SOURCES.items():
 image=ImageOps.exif_transpose(Image.open(ROOT/source)).convert('RGB')
 variants=[]
 for width in sorted({480,800,min(1280,image.width)}):
  height=round(image.height*width/image.width)
  destination=OUTPUT/f'{name}-{width}.webp'
  image.resize((width,height),Image.Resampling.LANCZOS).save(destination,quality=78,method=6)
  variants.append({'src':destination.relative_to(ROOT).as_posix(),'width':width,'height':height})
 manifest[name]={'source':source,'variants':variants}
(OUTPUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared',len(manifest),'real photographs; originals unchanged.')
