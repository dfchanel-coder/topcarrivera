"""Real photography and bilingual captions for the TOP CAR / BAIA update."""
import json
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
LIBRARY=json.loads((ROOT/'assets/photos/real/manifest.json').read_text(encoding='utf-8'))
PHOTOS={
 'taller-en-actividad':{
  'es':('Vehículos con el capó abierto en el taller TOP CAR de Rivera','El taller, en movimiento'),
  'pt':('Veículos com o capô aberto na oficina TOP CAR em Rivera','A oficina em atividade')},
 'frenos':{
  'es':('Disco y pinza de freno durante un trabajo en TOP CAR','Precisión en los detalles'),
  'pt':('Disco e pinça de freio durante um serviço na TOP CAR','Precisão nos detalhes')},
 'embrague':{
  'es':('Conjunto de embrague durante una intervención mecánica en TOP CAR','Mecánica de cerca'),
  'pt':('Conjunto de embreagem durante uma intervenção mecânica na TOP CAR','Mecânica de perto')},
 'fachada':{
  'es':('Entrada del taller TOP CAR en Rivera con vehículos frente al acceso','Nuestro lugar en Rivera'),
  'pt':('Entrada da oficina TOP CAR em Rivera com veículos em frente ao acesso','Nosso lugar em Rivera')},
 'interior':{
  'es':('Interior de TOP CAR con un vehículo en reparación y herramientas de taller','Donde pasa el trabajo'),
  'pt':('Interior da TOP CAR com um veículo em reparo e ferramentas da oficina','Onde o trabalho acontece')},
 'auxilio-baia':{
  'es':('Grúa de Auxilio BAIA transportando un automóvil sobre su plataforma','Auxilio BAIA · traslado de vehículos'),
  'pt':('Guincho do Auxilio BAIA transportando um automóvel na plataforma','Auxilio BAIA · transporte de veículos')},
}
REAL_COPY={
 'es':{
  'title':'TOP CAR Rivera | Taller mecánico y Auxilio BAIA 24 hs',
  'description':'Taller mecánico TOP CAR en Rivera: diagnóstico, frenos, motor y mantenimiento. Auxilio BAIA 24 hs y traslado de vehículos. Paysandú 255. Consultá por WhatsApp.',
  'illustrative':'TOP CAR · Taller real',
  'slidecaptions':['01 / NUESTRO TALLER. NUESTRO TRABAJO.','02 / PRECISIÓN EN CADA DETALLE.'],
  'emergencyeyebrow':'TOP CAR + AUXILIO BAIA',
  'emergencytext':'La trayectoria de BAIA en auxilio, ahora junto a TOP CAR. Asistencia 24 hs y traslado para autos, camionetas y camiones pequeños. Llamanos para coordinar y confirmar la cobertura según tu ubicación.',
  'galleryeyebrow':'EL TALLER, POR DENTRO',
  'gallerytitle':'FIERROS REALES.<br><span>TRABAJO DE VERDAD.</span>',
  'galleryintro':'Un vistazo a nuestro espacio y a los trabajos que pasan por TOP CAR. Fotos del taller, sin imágenes de stock.',
  'galleryhint':'Tocá una foto para verla completa.',
  'expand':'Ampliar foto', 'closephoto':'Cerrar foto', 'photoprev':'Foto anterior','photonext':'Foto siguiente',
  'waemergency':'Hola TOP CAR / Auxilio BAIA, necesito asistencia. Mi ubicación es: ',
 },
 'pt':{
  'title':'TOP CAR Rivera | Oficina mecânica e Auxilio BAIA 24h',
  'description':'Oficina TOP CAR em Rivera: diagnóstico, freios, motor e manutenção. Auxilio BAIA: socorro 24h e guincho. Paysandú 255, na fronteira. Consulte pelo WhatsApp.',
  'illustrative':'TOP CAR · Nossa oficina',
  'slidecaptions':['01 / NOSSA OFICINA. NOSSO TRABALHO.','02 / PRECISÃO EM CADA DETALHE.'],
  'emergencyeyebrow':'TOP CAR + AUXILIO BAIA',
  'emergencytext':'A experiência da BAIA em socorro, agora junto à TOP CAR. Assistência 24h e transporte para carros, caminhonetes e caminhões pequenos. Ligue para combinar o atendimento e confirmar a cobertura conforme sua localização.',
  'galleryeyebrow':'POR DENTRO DA OFICINA',
  'gallerytitle':'MOTORES REAIS.<br><span>TRABALHO DE VERDADE.</span>',
  'galleryintro':'Conheça nosso espaço e os trabalhos que passam pela TOP CAR. Fotos da própria oficina, sem imagens de banco.',
  'galleryhint':'Toque em uma foto para vê-la inteira.',
  'expand':'Ampliar foto', 'closephoto':'Fechar foto', 'photoprev':'Foto anterior','photonext':'Próxima foto',
  'waemergency':'Olá TOP CAR / Auxilio BAIA, preciso de assistência. Minha localização é: ',
 }
}

def photo(name,code,prefix,sizes,*,lazy=True,deferred=False):
 variants=LIBRARY[name]['variants']; largest=variants[-1]
 srcset=', '.join(f'{prefix}{v["src"]} {v["width"]}w' for v in variants)
 src_attribute='data-src' if deferred else 'src'
 set_attribute='data-srcset' if deferred else 'srcset'
 loading='decoding="async"' if deferred else ('loading="lazy" decoding="async"' if lazy else 'fetchpriority="high"')
 return f'<img {src_attribute}="{prefix}{largest["src"]}" {set_attribute}="{srcset}" sizes="{sizes}" width="{largest["width"]}" height="{largest["height"]}" alt="{escape(PHOTOS[name][code][0],quote=True)}" {loading}>'

def gallery(code,d,prefix):
 cards=[]
 for name in ['fachada','interior','embrague','frenos']:
  alt,caption=PHOTOS[name][code]; full=prefix+LIBRARY[name]['variants'][-1]['src']
  cards.append(f'<figure class="gallery-item"><a class="gallery-link" href="{full}" data-caption="{escape(caption,quote=True)}" aria-label="{d["expand"]}: {caption}">{photo(name,code,prefix,"(max-width: 600px) 85vw, (max-width: 1000px) 44vw, 23vw")}<span class="photo-expand" aria-hidden="true">↗</span></a><figcaption>{caption}</figcaption></figure>')
 return f'''<section class="section workshop-gallery" id="fotos" aria-labelledby="gallery-title"><div class="container"><div class="section-heading"><div><p class="eyebrow">{d['galleryeyebrow']}</p><h2 id="gallery-title">{d['gallerytitle']}</h2></div><p class="section-intro">{d['galleryintro']}</p></div><div class="gallery-grid">{''.join(cards)}</div><p class="gallery-hint">{d['galleryhint']}</p></div></section>
<dialog class="photo-dialog" aria-labelledby="photo-caption"><button type="button" class="photo-close" aria-label="{d['closephoto']}">×</button><figure><img class="photo-full" alt="" width="1280" height="960"><figcaption id="photo-caption" aria-live="polite"></figcaption></figure><div class="photo-navigation"><button type="button" data-photo-step="-1" aria-label="{d['photoprev']}">←</button><span class="photo-index" aria-hidden="true"></span><button type="button" data-photo-step="1" aria-label="{d['photonext']}">→</button></div></dialog>'''
