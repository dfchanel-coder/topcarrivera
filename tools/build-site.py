"""Build the two crawlable language pages; no runtime framework required."""
import json
from pathlib import Path
from html import escape
from urllib.parse import quote
from real_photos import REAL_COPY, PHOTOS, LIBRARY, photo, gallery

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://dfchanel-coder.github.io/topcarrivera/'
PHONE = '+59898738689'
MAP = 'https://www.google.com/maps/search/?api=1&query=Paysand%C3%BA+255%2C+Rivera%2C+Uruguay'

CONTENT = {
 'es': {
  'lang':'es-UY', 'title':'Taller mecánico en Rivera · TOP CAR | Auxilio 24 hs',
  'description':'Mecánica, diagnóstico con escáner, frenos y suspensión en Paysandú 255, Rivera. En la frontera con Livramento. Consultá por WhatsApp y auxilio 24 hs.',
  'skip':'Saltar al contenido', 'strap':'MECÁNICA AUTOMOTRIZ · RIVERA, UY', 'nav':['Servicios','El taller','Cómo trabajamos','Ubicación'],
  'book':'Agendar por WhatsApp', 'menu':'Abrir menú', 'heroeyebrow':'PASIÓN POR LOS FIERROS. PRECISIÓN EN CADA DETALLE.',
  'h1':'MECÁNICA<br>EN SERIO.<br><span>CONFIANZA</span><br>EN CADA KM.',
  'intro':'Tu taller mecánico en Rivera. Diagnóstico con criterio, herramientas profesionales y las cosas claras desde el primer momento.',
  'explore':'Conocé nuestros servicios', 'location':'Paysandú 255 · Rivera, Uruguay', 'hours':'Lun–Vie · 8:30–18:30',
  'slidealts':['Imagen ilustrativa: mecánico inspeccionando un motor en un taller','Imagen ilustrativa: trabajo de precisión con una llave en el motor'],
  'slidecaptions':['01 / EL DETALLE HACE LA DIFERENCIA','02 / LA HERRAMIENTA CORRECTA. EL CRITERIO TAMBIÉN.'],
  'illustrative':'Fotografías ilustrativas', 'pause':'Pausar imágenes', 'play':'Reanudar imágenes', 'previous':'Imagen anterior', 'next':'Imagen siguiente',
  'ribbon':['DIAGNÓSTICO CON ESCÁNER','PRESUPUESTO ANTES DE REPARAR','HERRAMIENTAS PROFESIONALES','AUXILIO 24 HS'],
  'serviceeyebrow':'01 / LO QUE HACEMOS', 'servicetitle':'TU AUTO HABLA.<br><span>SABEMOS ESCUCHARLO.</span>',
  'serviceintro':'Del mantenimiento de todos los días a esa falla que cuesta encontrar. Mecánica general para autos nacionales e importados.',
  'searchlabel':'¿Qué le pasa a tu auto?', 'searchplaceholder':'Probá “no arranca”, “frenos”, “barulho”…',
  'searchhelp':'Escribí el síntoma o el servicio, en español o portugués.', 'clear':'Limpiar búsqueda',
  'chips':['No arranca','Ruido al frenar','Pierde fuerza','Cambio de aceite'],
  'services':[
   ['Diagnóstico e inyección','ENTENDER ANTES DE CAMBIAR','Lectura de fallas con escáner, revisión de sensores, bobinas e inyección electrónica. Relacionamos los datos con lo que hace tu auto.','¿Prendió el check engine o perdió fuerza?','diagnostico'],
   ['Frenos y suspensión','SEGURIDAD EN CADA METRO','Pastillas, discos, líquido de frenos, amortiguadores, bujes y rótulas. Revisamos ruidos, vibraciones y el comportamiento al frenar.','¿Chilla al frenar o golpea en los pozos?','frenos'],
   ['Motor y transmisión','EL CORAZÓN DE TU AUTO','Mecánica general, embrague, distribución y transmisión. Evaluamos el origen del problema y te explicamos el trabajo necesario.','¿El motor falla o cuesta pasar los cambios?','motor'],
   ['Aceite y mantenimiento','CUIDAR HOY. SEGUIR MAÑANA.','Cambio de aceite y filtros, revisión de niveles y mantenimiento preventivo según las necesidades de tu vehículo.','¿Te toca el service o vas a salir a la ruta?','mantenimiento'],
   ['Electricidad y refrigeración','CADA SISTEMA, EN SU PUNTO','Batería y sistema de carga, radiador, bomba de agua, termostato y climatización. Buscamos la causa, no solo el síntoma.','¿No arranca, calienta o el aire no enfría?','electricidad'],
   ['Alineación y balanceo','QUE EL CAMINO SE SIENTA BIEN','Control de alineación y balanceo para atender vibraciones, desvíos y desgaste irregular de los neumáticos.','¿Vibra el volante o el auto se va de lado?','alineacion']
  ],
  'consult':'Consultar', 'noresults':'No encontramos una coincidencia. Contanos qué hace tu auto y te orientamos.',
  'searchdisclaimer':'Esta búsqueda orienta sobre servicios; el diagnóstico requiere revisar el vehículo.',
  'technicaleyebrow':'02 / CRITERIO TÉCNICO. OFICIO DE VERDAD.', 'technicaltitle':'NO ES ADIVINAR.<br>ES <span>DIAGNOSTICAR.</span>',
  'technicalintro':'Nos gustan los motores. Y más todavía, entender qué les pasa. En TOP CAR combinamos experiencia mecánica, equipamiento profesional y una forma de trabajar metódica.',
  'technicalpoints':[['Datos, no suposiciones','El escáner es el punto de partida. La inspección y el criterio mecánico completan el diagnóstico.'],['Herramientas para trabajar bien','Equipamiento profesional para revisar y reparar con precisión. Cada trabajo tiene su procedimiento.'],['Explicaciones que se entienden','Te contamos qué encontramos, qué hace falta y cuánto cuesta antes de comenzar.']],
  'technicalstamp':'PRECISIÓN<br>QUE SE NOTA.', 'processlabel':'03 / ASÍ TRABAJAMOS', 'processtitle':'MENOS VUELTAS.<br><span>MÁS CLARIDAD.</span>',
  'steps':[['Nos contás qué pasa','Escribinos con la marca, el modelo y el síntoma. Coordinamos la revisión.'],['Revisamos y presupuestamos','Inspeccionamos el vehículo, explicamos el diagnóstico y acordamos el trabajo con vos.'],['Reparamos y verificamos','Hacemos la reparación y los controles correspondientes antes de entregar.']],
  'emergencyeyebrow':'CUANDO EL AUTO NO PUEDE SEGUIR', 'emergencytitle':'EL AUXILIO<br>NO MIRA <span>LA HORA.</span>',
  'emergencytext':'Auxilio 24 hs para autos, camionetas y camiones pequeños. Llamanos y contanos dónde estás para coordinar la asistencia y confirmar la cobertura.',
  'call':'Llamar ahora', 'emergencynote':'Para una emergencia, llamá directamente.',
  'borderlabel':'04 / DE ACÁ. DE LA FRONTERA.', 'bordertitle':'RIVERA &<br><span>LIVRAMENTO.</span>',
  'bordertext':'Acá conviven el español, el portugués y las mil formas de hablar de un auto. Si buscás un taller mecánico en Rivera o una oficina mecânica cerca de Santana do Livramento, encontranos del lado uruguayo, en Paysandú 255.',
  'borderterms':'Frenos o freios. Embrague o embreagem. Mantenimiento o revisão. Lo importante es entender qué necesita tu vehículo.',
  'borderlink':'Ver a página em português', 'borderlanguage':'pt-BR', 'borderquestion':'¿Venís desde Livramento?',
  'borderanswer':'Coordiná tu visita por WhatsApp antes de venir. Para auxilio, consultá la cobertura según tu ubicación; no asumimos asistencia del lado brasileño.',
  'locationlabel':'05 / NOS ENCONTRÁS ACÁ', 'locationtitle':'TU TALLER.<br><span>EN RIVERA.</span>', 'addresslabel':'DIRECCIÓN', 'hourslabel':'HORARIO DEL TALLER',
  'hoursfull':'Lunes a viernes, de 8:30 a 18:30.', 'weekend':'Sábados y domingos cerrado. Auxilio 24 hs.', 'directions':'Cómo llegar', 'maptitle':'Ubicación de TOP CAR en Rivera',
  'mapload':'Cargar mapa interactivo', 'mapprivacy':'El mapa se carga desde Google solo si lo abrís.',
  'faqlabel':'06 / RESPUESTAS CLARAS', 'faqtitle':'ANTES DE<br><span>TRAER TU AUTO.</span>',
  'faqs':[
   ['¿Dónde queda TOP CAR en Rivera?','El taller está en Paysandú 255, Rivera, Uruguay, en la ciudad fronteriza con Santana do Livramento, Brasil. Podés abrir la ubicación y las indicaciones desde esta página.'],
   ['¿Qué servicios de mecánica realizan?','Mecánica general, motor, embrague y transmisión; diagnóstico con escáner e inyección electrónica; frenos y suspensión; alineación y balanceo; aceite y filtros; batería, refrigeración y aire acondicionado. Consultá por tu modelo y el trabajo que necesitás.'],
   ['Mi auto no arranca o pierde fuerza, ¿lo pueden revisar?','Sí. Contanos si no gira el motor, si gira pero no enciende, si se apaga o si perdió fuerza. Esos detalles ayudan a coordinar la revisión. El origen de la falla se confirma inspeccionando el vehículo.'],
   ['¿Tienen auxilio mecánico las 24 horas?','Sí, TOP CAR ofrece auxilio 24 hs para autos, camionetas y camiones pequeños. Llamá al +598 98 738 689 y compartí tu ubicación para confirmar la disponibilidad y la cobertura.'],
   ['¿Puedo coordinar una visita desde Santana do Livramento?','Sí, podés consultar y coordinar por WhatsApp. El taller está en Rivera, del lado uruguayo. La cobertura del auxilio debe confirmarse según la ubicación; no se promete servicio en Brasil.'],
   ['¿Cómo pido un presupuesto y cuál es el horario?','Escribí al WhatsApp +598 98 738 689 con marca, modelo y el problema del vehículo. Coordinamos el diagnóstico y te explicamos el presupuesto antes de reparar. El horario habitual es de lunes a viernes de 8:30 a 18:30; consultá por feriados.']
  ],
  'ctatitle':'CONTANOS QUÉ PASA.<br><span>NOS PONEMOS EN MARCHA.</span>', 'ctatext':'Marca, modelo y ese ruido que no sabés cómo explicar. Empezamos por escucharte.',
  'email':'Enviar un e-mail', 'footer':'Mecánica con criterio. Atención de acá.', 'credit':'Diseño y desarrollo',
  'wanormal':'Hola TOP CAR, quiero coordinar una revisión. Mi auto es: ', 'waemergency':'Hola TOP CAR, necesito auxilio. Mi ubicación es: ',
 },
 'pt': {
  'lang':'pt-BR', 'title':'Oficina mecânica em Rivera · TOP CAR | Socorro 24h',
  'description':'Oficina mecânica em Rivera, na fronteira com Santana do Livramento. Diagnóstico, freios, suspensão e manutenção. Paysandú 255. Agende pelo WhatsApp.',
  'skip':'Pular para o conteúdo', 'strap':'MECÂNICA AUTOMOTIVA · RIVERA, UY', 'nav':['Serviços','A oficina','Como trabalhamos','Localização'],
  'book':'Agendar pelo WhatsApp', 'menu':'Abrir menu', 'heroeyebrow':'PAIXÃO POR MOTORES. PRECISÃO EM CADA DETALHE.',
  'h1':'MECÂNICA<br>DE VERDADE.<br><span>CONFIANÇA</span><br>EM CADA KM.',
  'intro':'Sua oficina mecânica em Rivera. Diagnóstico criterioso, ferramentas profissionais e tudo explicado desde o primeiro contato.',
  'explore':'Conheça nossos serviços', 'location':'Paysandú 255 · Rivera, Uruguai', 'hours':'Seg–Sex · 8h30–18h30',
  'slidealts':['Imagem ilustrativa: mecânico inspecionando o motor em uma oficina','Imagem ilustrativa: trabalho de precisão com uma chave no motor'],
  'slidecaptions':['01 / O DETALHE FAZ A DIFERENÇA','02 / A FERRAMENTA CERTA. O CRITÉRIO TAMBÉM.'],
  'illustrative':'Fotografias ilustrativas', 'pause':'Pausar imagens', 'play':'Retomar imagens', 'previous':'Imagem anterior', 'next':'Próxima imagem',
  'ribbon':['DIAGNÓSTICO COM SCANNER','ORÇAMENTO ANTES DO REPARO','FERRAMENTAS PROFISSIONAIS','SOCORRO 24H'],
  'serviceeyebrow':'01 / O QUE FAZEMOS', 'servicetitle':'SEU CARRO FALA.<br><span>A GENTE ENTENDE.</span>',
  'serviceintro':'Da manutenção do dia a dia à falha difícil de encontrar. Mecânica geral para carros nacionais e importados.',
  'searchlabel':'O que está acontecendo com seu carro?', 'searchplaceholder':'Experimente “não pega”, “freios”, “barulho”…',
  'searchhelp':'Digite o sintoma ou serviço, em português ou espanhol.', 'clear':'Limpar busca',
  'chips':['Não pega','Barulho ao frear','Perde força','Troca de óleo'],
  'services':[
   ['Diagnóstico e injeção','ENTENDER ANTES DE TROCAR','Leitura de falhas com scanner, inspeção de sensores, bobinas e injeção eletrônica. Relacionamos os dados com o comportamento do carro.','A luz da injeção acendeu ou perdeu força?','diagnostico'],
   ['Freios e suspensão','SEGURANÇA A CADA METRO','Pastilhas, discos, fluido de freio, amortecedores, buchas e pivôs. Verificamos ruídos, vibrações e o comportamento ao frear.','Faz barulho ao frear ou nas irregularidades?','frenos'],
   ['Motor e transmissão','O CORAÇÃO DO SEU CARRO','Mecânica geral, embreagem, distribuição e transmissão. Avaliamos a origem do problema e explicamos o reparo necessário.','O motor falha ou está difícil trocar de marcha?','motor'],
   ['Óleo e manutenção','CUIDAR HOJE. SEGUIR AMANHÃ.','Troca de óleo e filtros, verificação de níveis e manutenção preventiva conforme as necessidades do seu veículo.','Está na hora da revisão ou vai pegar a estrada?','mantenimiento'],
   ['Elétrica e arrefecimento','CADA SISTEMA, NO SEU PONTO','Bateria e sistema de carga, radiador, bomba d’água, válvula termostática e climatização. Buscamos a causa, não só o sintoma.','Não pega, esquenta ou o ar não gela?','electricidad'],
   ['Alinhamento e balanceamento','PARA SEGUIR NO CAMINHO CERTO','Verificação de alinhamento e balanceamento para tratar vibrações, desvios e desgaste irregular dos pneus.','O volante vibra ou o carro puxa para o lado?','alineacion']
  ],
  'consult':'Consultar', 'noresults':'Não encontramos uma correspondência. Conte o que seu carro está fazendo para orientarmos você.',
  'searchdisclaimer':'A busca orienta sobre serviços; o diagnóstico exige a inspeção do veículo.',
  'technicaleyebrow':'02 / CRITÉRIO TÉCNICO. EXPERIÊNCIA DE VERDADE.', 'technicaltitle':'NÃO É ADIVINHAR.<br>É <span>DIAGNOSTICAR.</span>',
  'technicalintro':'Gostamos de motores. E ainda mais de entender o que acontece com eles. Na TOP CAR, combinamos experiência mecânica, equipamentos profissionais e um trabalho metódico.',
  'technicalpoints':[['Dados, não suposições','O scanner é o ponto de partida. A inspeção e o critério mecânico completam o diagnóstico.'],['Ferramentas para trabalhar bem','Equipamentos profissionais para verificar e reparar com precisão. Cada serviço tem seu procedimento.'],['Explicações que fazem sentido','Explicamos o que encontramos, o que precisa ser feito e quanto custa antes de começar.']],
  'technicalstamp':'PRECISÃO<br>QUE SE SENTE.', 'processlabel':'03 / COMO TRABALHAMOS', 'processtitle':'MENOS COMPLICAÇÃO.<br><span>MAIS CLAREZA.</span>',
  'steps':[['Você conta o que acontece','Envie marca, modelo e o sintoma pelo WhatsApp. Combinamos a inspeção.'],['Inspeção e orçamento','Verificamos o veículo, explicamos o diagnóstico e combinamos o serviço com você.'],['Reparo e verificação','Executamos o reparo e os controles correspondentes antes da entrega.']],
  'emergencyeyebrow':'QUANDO O CARRO NÃO PODE SEGUIR', 'emergencytitle':'O SOCORRO<br>NÃO OLHA <span>A HORA.</span>',
  'emergencytext':'Socorro 24h para carros, caminhonetes e caminhões pequenos. Ligue e informe onde está para coordenar a assistência e confirmar a cobertura.',
  'call':'Ligar agora', 'emergencynote':'Em uma emergência, ligue diretamente.',
  'borderlabel':'04 / DAQUI. DA FRONTEIRA.', 'bordertitle':'RIVERA &<br><span>LIVRAMENTO.</span>',
  'bordertext':'Aqui convivem o português, o espanhol e muitos jeitos de falar de um carro. Se procura uma oficina mecânica em Rivera ou perto de Santana do Livramento, estamos do lado uruguaio, na Paysandú 255.',
  'borderterms':'Freios ou frenos. Embreagem ou embrague. Revisão ou mantenimiento. O importante é entender o que seu veículo precisa.',
  'borderlink':'Ver la página en español', 'borderlanguage':'es-UY', 'borderquestion':'Vem de Santana do Livramento?',
  'borderanswer':'Combine sua visita pelo WhatsApp antes de vir. Para socorro, consulte a cobertura conforme sua localização; não presumimos atendimento do lado brasileiro.',
  'locationlabel':'05 / ENCONTRE A GENTE', 'locationtitle':'SUA OFICINA.<br><span>EM RIVERA.</span>', 'addresslabel':'ENDEREÇO', 'hourslabel':'HORÁRIO DA OFICINA',
  'hoursfull':'Segunda a sexta, das 8h30 às 18h30.', 'weekend':'Sábados e domingos fechado. Socorro 24h.', 'directions':'Como chegar', 'maptitle':'Localização da TOP CAR em Rivera',
  'mapload':'Carregar mapa interativo', 'mapprivacy':'O mapa do Google só é carregado se você abrir.',
  'faqlabel':'06 / RESPOSTAS CLARAS', 'faqtitle':'ANTES DE<br><span>TRAZER SEU CARRO.</span>',
  'faqs':[
   ['Onde fica a TOP CAR em Rivera?','A oficina fica na Paysandú 255, Rivera, Uruguai, na cidade que faz fronteira com Santana do Livramento, Brasil. Você pode abrir o mapa e as rotas nesta página.'],
   ['Quais serviços de mecânica vocês realizam?','Mecânica geral, motor, embreagem e transmissão; diagnóstico com scanner e injeção eletrônica; freios e suspensão; alinhamento e balanceamento; óleo e filtros; bateria, arrefecimento e ar-condicionado. Consulte sobre seu modelo e o serviço necessário.'],
   ['Meu carro não pega ou perde força. Vocês verificam?','Sim. Conte se o motor não gira, gira mas não pega, apaga ou perdeu força. Esses detalhes ajudam a combinar a inspeção. A origem da falha é confirmada verificando o veículo.'],
   ['Vocês oferecem socorro mecânico 24 horas?','Sim, a TOP CAR oferece socorro 24h para carros, caminhonetes e caminhões pequenos. Ligue para +598 98 738 689 e informe sua localização para confirmar disponibilidade e cobertura.'],
   ['Posso agendar uma visita vindo de Santana do Livramento?','Sim, consulte e agende pelo WhatsApp. A oficina fica em Rivera, do lado uruguaio. A cobertura do socorro precisa ser confirmada conforme a localização; não há promessa de atendimento no Brasil.'],
   ['Como pedir um orçamento e qual é o horário?','Envie marca, modelo e o problema do veículo pelo WhatsApp +598 98 738 689. Combinamos o diagnóstico e explicamos o orçamento antes do reparo. O horário habitual é de segunda a sexta, das 8h30 às 18h30; consulte sobre feriados.']
  ],
  'ctatitle':'CONTE O QUE ACONTECE.<br><span>A GENTE ENTRA EM AÇÃO.</span>', 'ctatext':'Marca, modelo e aquele barulho difícil de explicar. Começamos ouvindo você.',
  'email':'Enviar um e-mail', 'footer':'Mecânica com critério. Atendimento daqui.', 'credit':'Design e desenvolvimento',
  'wanormal':'Olá TOP CAR, quero agendar uma revisão. Meu carro é: ', 'waemergency':'Olá TOP CAR, preciso de socorro. Minha localização é: ',
 }
}

for code, updates in REAL_COPY.items():
 CONTENT[code].update(updates)
 question, answer = CONTENT[code]['faqs'][3]
 CONTENT[code]['faqs'][3] = [question, answer.replace('TOP CAR ofrece auxilio 24 hs', 'TOP CAR y Auxilio BAIA ofrecen asistencia y traslado 24 hs').replace('a TOP CAR oferece socorro 24h', 'a TOP CAR e o Auxilio BAIA oferecem socorro e transporte 24h')]

ICONS = [
 '<rect x="3" y="3" width="18" height="13" rx="2"/><path d="M8 21h8M12 16v5M6 10h3l2-4 3 7 2-3h2"/>',
 '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><path d="m7 5 2 3m8-3-2 3m-8 11 2-3m8 3-2-3"/>',
 '<path d="M7 5h9v3h4v10H5v-3H2V9h3V8h2ZM9 2h5M11 2v3m11 6v4M8 11h5v4"/>',
 '<path d="M12 2C9 7 5 11 5 15a7 7 0 0 0 14 0c0-4-4-8-7-13Z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
 '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M7 3v3m10-3v3M6 12h4m-2-2v4m6-2h4"/>',
 '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><path d="M12 3v6m0 6v6M3 12h6m6 0h6"/>'
]
def icon(i):
 return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[i]}</svg>'
def wa(message): return 'https://wa.me/59898738689?text=' + quote(message)
def build(code, d):
 prefix = '../' if code == 'pt' else ''
 url = BASE + ('pt/' if code == 'pt' else '')
 other = '../' if code == 'pt' else 'pt/'
 normal = wa(d['wanormal'])
 biz = {'@type':'AutoRepair','@id':BASE+'#business','name':'TOP CAR — Mecánica Automotriz','alternateName':'TOP CAR Rivera','url':BASE,
  'logo':BASE+'assets/icon-512.png','image':[BASE+LIBRARY[name]['variants'][-1]['src'] for name in ['taller-en-actividad','fachada','auxilio-baia']], 'telephone':PHONE,'email':'jonahiggie@gmail.com',
  'description':d['description'], 'address':{'@type':'PostalAddress','streetAddress':'Paysandú 255','addressLocality':'Rivera','addressRegion':'Rivera','postalCode':'40000','addressCountry':'UY'},
  'hasMap':MAP,'areaServed':{'@type':'City','name':'Rivera, Uruguay'},
  'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':['Monday','Tuesday','Wednesday','Thursday','Friday'],'opens':'08:30','closes':'18:30'}],
  'sameAs':['https://www.instagram.com/topcar.rivera/','https://www.facebook.com/1347989881946981'],
  'hasOfferCatalog':{'@type':'OfferCatalog','name':d['nav'][0],'itemListElement':[{'@type':'Offer','itemOffered':{'@type':'Service','name':s[0],'description':s[2],'provider':{'@id':BASE+'#business'}}} for s in d['services']]}}
 biz['hasOfferCatalog']['itemListElement'].append({'@type':'Offer','itemOffered':{'@type':'Service','name':'Auxilio BAIA — '+('socorro e guincho 24h' if code=='pt' else 'auxilio y traslado 24 hs'),'description':d['emergencytext'],'provider':{'@id':BASE+'#business'}}})
 schema={'@context':'https://schema.org','@graph':[biz,{'@type':'WebSite','@id':BASE+'#website','url':BASE,'name':'TOP CAR Rivera','inLanguage':['es-UY','pt-BR'],'publisher':{'@id':BASE+'#business'}},
  {'@type':'WebPage','@id':url+'#webpage','url':url,'name':d['title'],'description':d['description'],'inLanguage':d['lang'],'isPartOf':{'@id':BASE+'#website'},'about':{'@id':BASE+'#business'}},
  {'@type':'FAQPage','@id':url+'#faq','inLanguage':d['lang'],'mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in d['faqs']]}]}
 nav = ''.join(f'<a href="#{anchor}">{label}</a>' for anchor,label in zip(['servicios','taller','proceso','ubicacion'],d['nav']))
 cards = ''.join(f'''<article class="service-card" id="{s[4]}" data-service="{s[4]}"><div class="service-top">{icon(i)}<span>0{i+1}</span></div><p class="micro">{s[1]}</p><h3>{s[0]}</h3><p>{s[2]}</p><div class="service-bottom"><p>{s[3]}</p><a href="{wa(('Olá TOP CAR, quero consultar sobre: ' if code=='pt' else 'Hola TOP CAR, quiero consultar por: ')+s[0])}" target="_blank" rel="noopener" aria-label="{d['consult']}: {s[0]}">{d['consult']} <span aria-hidden="true">↗</span></a></div></article>''' for i,s in enumerate(d['services']))
 points=''.join(f'<li><span class="point-index">0{i+1}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for i,(t,p) in enumerate(d['technicalpoints']))
 steps=''.join(f'<li><span class="step-number">0{i+1}</span><h3>{t}</h3><p>{p}</p></li>' for i,(t,p) in enumerate(d['steps']))
 faqs=''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in d['faqs'])
 slides=''.join(f'<figure class="hero-slide{" is-active" if i==0 else ""}" aria-hidden="{"false" if i==0 else "true"}">{photo(name,code,prefix,"(max-width:760px) 100vw, 58vw",lazy=False,deferred=i>0)}<figcaption>{d["slidecaptions"][i]}</figcaption></figure>' for i,name in enumerate(['taller-en-actividad','frenos']))
 gallery_html=gallery(code,d,prefix)

 html=f'''<!doctype html>
<html lang="{d['lang']}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['title']}</title><meta name="description" content="{d['description']}">
<meta name="robots" content="index,follow,max-image-preview:large"><meta name="theme-color" content="#111314">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="es-UY" href="{BASE}"><link rel="alternate" hreflang="pt-BR" href="{BASE}pt/"><link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website"><meta property="og:locale" content="{d['lang'].replace('-','_')}"><meta property="og:locale:alternate" content="{'es_UY' if code=='pt' else 'pt_BR'}"><meta property="og:site_name" content="TOP CAR Rivera"><meta property="og:title" content="{d['title']}"><meta property="og:description" content="{d['description']}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}assets/og-image.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:alt" content="TOP CAR · Rivera · {d['ribbon'][3]}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{d['title']}"><meta name="twitter:description" content="{d['description']}"><meta name="twitter:image" content="{BASE}assets/og-image.jpg"><meta name="twitter:image:alt" content="TOP CAR · Rivera · {d['ribbon'][3]}">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="{prefix}assets/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png"><link rel="manifest" href="{prefix}site.webmanifest">
<link rel="preload" href="{prefix}assets/fonts/barlow-condensed-800.woff" as="font" type="font/woff" crossorigin><link rel="stylesheet" href="{prefix}css/styles.css">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False,separators=(',',':'))}</script>
<script src="{prefix}js/main.js" defer></script></head>
<body><a class="skip-link" href="#contenido">{d['skip']}</a>
<div class="topline"><div class="container"><span>{d['strap']}</span><a href="tel:{PHONE}"><span class="live-dot"></span>{d['ribbon'][3]} <span class="top-phone"> / 098 738 689</span> <span aria-hidden="true">↗</span></a></div></div>
<header class="site-header"><div class="container nav-row"><a class="brand" href="{prefix or './'}"><span class="brand-slashes" aria-hidden="true">///</span>TOP<span>CAR</span><small>{'MECÂNICA AUTOMOTIVA' if code=='pt' else 'MECÁNICA AUTOMOTRIZ'}</small></a><nav id="mainNav" aria-label="{'Navegação principal' if code=='pt' else 'Navegación principal'}">{nav}</nav><div class="nav-actions"><div class="languages" aria-label="{'Idioma' if code=='pt' else 'Idioma'}"><a href="{prefix or './'}" lang="es-UY" hreflang="es-UY" {'aria-current="page"' if code=='es' else ''}>ES</a><span>/</span><a href="{'./' if code=='pt' else 'pt/'}" lang="pt-BR" hreflang="pt-BR" {'aria-current="page"' if code=='pt' else ''}>PT</a></div><a class="btn btn-small nav-book" href="{normal}" target="_blank" rel="noopener">WhatsApp <span aria-hidden="true">↗</span></a><button class="menu-toggle" aria-label="{d['menu']}" aria-controls="mainNav" aria-expanded="false" hidden><span></span><span></span></button></div></div></header>
<main id="contenido"><section class="hero" id="inicio" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow"><span></span>{d['heroeyebrow']}</p><h1 id="hero-title">{d['h1']}</h1><p class="hero-intro">{d['intro']}</p><div class="hero-actions"><a class="btn" href="{normal}" target="_blank" rel="noopener">{d['book']} <span aria-hidden="true">↗</span></a><a class="text-link" href="#servicios">{d['explore']} <span aria-hidden="true">↓</span></a></div><div class="hero-location"><span class="crosshair" aria-hidden="true">⊕</span><div><a href="#ubicacion">{d['location']}</a><span>{d['hours']}</span></div></div></div>
<div class="hero-media" role="region" aria-roledescription="{'carrossel' if code=='pt' else 'carrusel'}" aria-label="{'Mecânica em detalhe' if code=='pt' else 'Mecánica en detalle'}">{slides}<div class="photo-corner"><span>TOP CAR / TECHNICAL CARE</span><span class="corner-cross" aria-hidden="true">+</span></div><div class="hero-photo-label">{d['illustrative']}</div><div class="carousel-controls" hidden><span class="slide-count" aria-live="off">01 <span>/ 02</span></span><button data-carousel="previous" aria-label="{d['previous']}">←</button><button data-carousel="pause" aria-label="{d['pause']}" data-pause="{d['pause']}" data-play="{d['play']}"><span aria-hidden="true">Ⅱ</span></button><button data-carousel="next" aria-label="{d['next']}">→</button></div><div class="hero-media-rule" aria-hidden="true"></div></div></section>
<div class="trust-strip"><div class="container">{''.join(f'<span><i aria-hidden="true">+</i>{x}</span>' for x in d['ribbon'])}</div></div>
<section class="section services" id="servicios" aria-labelledby="services-title"><div class="container"><div class="section-heading"><div><p class="eyebrow">{d['serviceeyebrow']}</p><h2 id="services-title">{d['servicetitle']}</h2></div><p class="section-intro">{d['serviceintro']}</p></div><div class="service-search" hidden><label for="service-query">{d['searchlabel']}</label><div class="search-box"><span aria-hidden="true">⌕</span><input id="service-query" type="search" placeholder="{d['searchplaceholder']}" aria-describedby="search-help" maxlength="100" autocomplete="off"><button id="clear-search" aria-label="{d['clear']}">×</button></div><p id="search-help">{d['searchhelp']}</p><div class="search-chips">{''.join(f'<button type="button" data-query="{x}">{x}<span aria-hidden="true">↗</span></button>' for x in d['chips'])}</div><p class="sr-only" id="search-status" role="status"></p></div><div class="service-grid">{cards}</div><div class="no-results" hidden><p>{d['noresults']}</p><a class="text-link" href="{normal}" target="_blank" rel="noopener">WhatsApp ↗</a></div><p class="search-note" hidden>{d['searchdisclaimer']}</p></div></section>
<section class="section technical" id="taller" aria-labelledby="technical-title"><div class="container technical-grid"><div class="technical-photo">{photo('embrague',code,prefix,'(max-width:760px) 90vw, 45vw')}<span class="image-note">{d['illustrative']}</span><div class="photo-stamp">{d['technicalstamp']}<span aria-hidden="true">↗</span></div></div><div class="technical-copy"><p class="eyebrow">{d['technicaleyebrow']}</p><h2 id="technical-title">{d['technicaltitle']}</h2><p>{d['technicalintro']}</p><ul class="technical-points">{points}</ul></div></div></section>
{gallery_html}
<section class="section process" id="proceso"><div class="container"><div class="section-heading"><div><p class="eyebrow">{d['processlabel']}</p><h2>{d['processtitle']}</h2></div><a class="text-link" href="{normal}" target="_blank" rel="noopener">{d['book']} ↗</a></div><ol class="steps">{steps}</ol></div></section>
<section class="emergency" id="auxilio" aria-labelledby="emergency-title"><div class="container emergency-grid"><div><p class="eyebrow">{d['emergencyeyebrow']}</p><h2 id="emergency-title">{d['emergencytitle']}</h2><p>{d['emergencytext']}</p><div class="emergency-actions"><a class="btn btn-white" href="tel:{PHONE}">{d['call']} <span aria-hidden="true">↗</span></a><a class="text-link" href="{wa(d['waemergency'])}" target="_blank" rel="noopener">WhatsApp ↗</a></div><small>{d['emergencynote']}</small></div><figure class="emergency-photo">{photo('auxilio-baia',code,prefix,'(max-width:760px) 90vw, 48vw')}<figcaption><strong>AUXILIO BAIA</strong><span>{'ASISTENCIA Y TRASLADO · 24 HS' if code=='es' else 'SOCORRO E TRANSPORTE · 24H'}</span></figcaption></figure></div></section>
<section class="section border-section" id="frontera"><div class="container border-grid"><div><p class="eyebrow">{d['borderlabel']}</p><h2>{d['bordertitle']}</h2><div class="border-coordinate"><span>UY</span><span class="border-line"></span><span>BR</span></div></div><div class="border-copy"><p>{d['bordertext']}</p><p class="border-terms">{d['borderterms']}</p><a class="text-link" href="{other}" lang="{d['borderlanguage']}" hreflang="{d['borderlanguage']}">{d['borderlink']} ↗</a><div class="border-visit"><h3>{d['borderquestion']}</h3><p>{d['borderanswer']}</p></div></div></div></section>
<section class="section location" id="ubicacion"><div class="container location-grid"><div><p class="eyebrow">{d['locationlabel']}</p><h2>{d['locationtitle']}</h2><div class="location-detail"><span class="micro">{d['addresslabel']}</span><address>Paysandú 255<br>Rivera, Uruguay</address></div><div class="location-detail"><span class="micro">{d['hourslabel']}</span><p>{d['hoursfull']}<br><small>{d['weekend']}</small></p><p class="open-status" id="openStatus" aria-live="polite"></p></div><a class="text-link" href="tel:{PHONE}">+598 98 738 689 ↗</a></div><div class="map-card"><div class="map-grid" aria-hidden="true"><div class="map-road road-one"></div><div class="map-road road-two"></div><div class="map-pin">TC<span></span></div><span class="map-street">PAYSANDÚ 255</span><span class="map-city">RIVERA / UY</span></div><div class="map-caption"><strong>TOP CAR</strong><a class="btn btn-small" href="{MAP}" target="_blank" rel="noopener">{d['directions']} ↗</a></div><div class="map-slot" id="map-slot"></div><button class="map-load" data-title="{d['maptitle']}" hidden>{d['mapload']} <span aria-hidden="true">+</span></button><p class="map-privacy">{d['mapprivacy']}</p></div></div></section>
<section class="section faq" id="faq"><div class="container faq-grid"><div><p class="eyebrow">{d['faqlabel']}</p><h2>{d['faqtitle']}</h2></div><div class="faq-list">{faqs}</div></div></section>
<section class="closing" id="contacto"><div class="container"><p class="eyebrow">TOP CAR / RIVERA</p><h2>{d['ctatitle']}</h2><p>{d['ctatext']}</p><div class="closing-actions"><a class="btn" href="{normal}" target="_blank" rel="noopener">{d['book']} ↗</a><a class="text-link" href="mailto:jonahiggie@gmail.com">{d['email']} ↗</a></div></div></section></main>
<footer><div class="container footer-main"><div><a class="brand" href="{prefix or './'}">TOP<span>CAR</span></a><p>{d['footer']}</p></div><nav aria-label="{'Links do rodapé' if code=='pt' else 'Enlaces del pie'}">{nav}</nav><div class="footer-social"><a href="https://www.instagram.com/topcar.rivera/" target="_blank" rel="noopener">Instagram ↗</a><a href="https://www.facebook.com/1347989881946981" target="_blank" rel="noopener">Facebook ↗</a><a href="{normal}" target="_blank" rel="noopener">WhatsApp ↗</a></div></div><div class="container footer-bottom"><span>© <span id="year">2026</span> TOP CAR · Rivera, Uruguay</span><span>{'Fotos de nuestro taller y auxilio' if code=='es' else 'Fotos da nossa oficina e do socorro'}</span><span>{d['credit']}: <a href="https://www.fbinformaticauy.com" target="_blank" rel="noopener">FB Informática ↗</a></span></div></footer>
<div class="mobile-contact"><a href="tel:{PHONE}">{d['ribbon'][3]} ↗</a><a href="{normal}" target="_blank" rel="noopener">WhatsApp ↗</a></div>
</body></html>'''
 dest=ROOT / ('pt/index.html' if code=='pt' else 'index.html')
 dest.parent.mkdir(exist_ok=True)
 dest.write_text(html,encoding='utf-8')

if __name__ == '__main__':
 for code,data in CONTENT.items(): build(code,data)
 entries='\n'.join(f'''  <url>
    <loc>{BASE}{suffix}</loc>
    <lastmod>2026-11-02</lastmod>
    <xhtml:link rel="alternate" hreflang="es-UY" href="{BASE}" />
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{BASE}pt/" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}" />
    {''.join('<image:image><image:loc>'+BASE+LIBRARY[name]['variants'][-1]['src']+'</image:loc></image:image>' for name in LIBRARY)}
  </url>''' for suffix in ['', 'pt/'])
 (ROOT/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml"\n        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n{entries}\n</urlset>\n',encoding='utf-8')
 (ROOT/'robots.txt').write_text(f'''# TOP CAR - Rivera, Uruguay
# Public search and AI crawlers may access public content and rendering assets.
# robots.txt must be served at the origin root to be effective.
User-agent: *
Allow: /

Sitemap: {BASE}sitemap.xml
''',encoding='utf-8')
 lines=['# TOP CAR — Mecánica Automotriz en Rivera', '', '> Taller mecánico en Paysandú 255, Rivera, Uruguay. Oficina mecânica em Rivera, na fronteira com Santana do Livramento.','', '## Páginas oficiales', f'- [Español]({BASE})',f'- [Português]({BASE}pt/)','','## Contacto y ubicación','- Dirección: Paysandú 255, Rivera, Uruguay.','- Teléfono y WhatsApp: +598 98 738 689.','- E-mail: jonahiggie@gmail.com.','- Horario habitual: lunes a viernes de 08:30 a 18:30, America/Montevideo. Consultar feriados.','- Sábados y domingos: taller cerrado. Auxilio 24 hs para autos, camionetas y camiones pequeños.','- Confirmar disponibilidad y cobertura del auxilio por teléfono. No se declara cobertura en Brasil.','- El local está en Uruguay, no en Santana do Livramento.','','## Servicios']
 for es,pt in zip(CONTENT['es']['services'],CONTENT['pt']['services']): lines.append(f'- {es[0]} / {pt[0]}: {es[2]}')
 lines += ['', '## Auxilio BAIA', 'TOP CAR incorpora el nombre Auxilio BAIA, un servicio de grúa y auxilio con trayectoria en Rivera. Asistencia 24 hs y traslado de vehículos. Coordinar disponibilidad y cobertura al +598 98 738 689.', '', '## Preguntas y respuestas']
 for question,answer in CONTENT['es']['faqs']: lines += [f'### {question}',answer,'']
 lines += ['## Alcance de la información','- Fotografías reales del taller, trabajos mecánicos y grúa de Auxilio BAIA, proporcionadas por el negocio.','- No se publican títulos de ingeniería, certificaciones, precios, marcas de herramientas ni calificaciones sin verificar.','- El diagnóstico y el presupuesto dependen de la inspección del vehículo.','- Este resumen facilita la lectura; no garantiza indexación, posicionamiento ni citas por asistentes.']
 (ROOT/'llms.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print('Built index.html and pt/index.html')
