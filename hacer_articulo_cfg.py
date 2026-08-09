import re
tpl=open('blog/fondos-indexados-guia-2026.html',encoding='utf-8').read()
nuevo=open('contenido_articulo_cfg.html',encoding='utf-8').read().strip()
slug='como-empezar-a-ahorrar-e-invertir'
TITLE='Cómo empezar a ahorrar e invertir desde cero'
DESC='Aprende a ahorrar e invertir desde cero con un camino sencillo y efectivo: presupuesto, fondo de emergencia e inversión a largo plazo.'

# 1) title
tpl=re.sub(r'<title>.*?</title>','<title>'+TITLE+'</title>',tpl,count=1,flags=re.S)
# 2) meta description (primera)
tpl=re.sub(r'(<meta\s+name="description"\s+content=")[^"]*(")', r'\g<1>'+DESC+r'\g<2>', tpl, count=1, flags=re.I)
# 3) contenido: reemplazar desde el <h1> hasta el <footer> (o </body>)
hi=tpl.find('<h1')
fi=tpl.find('<footer')
if fi==-1: fin=tpl.rfind('</body>')
else:
    # buscar el cierre del footer: </footer>
    fc=tpl.find('</footer>')
    fin=fc+len('</footer>') if fc!=-1 else fi
if hi==-1: raise SystemExit('no h1')
pre=tpl[:hi]
post=tpl[fin:] if fin>hi else tpl[hi:]
nuevo2=re.sub(r'<h1[^>]*>.*?</h1>','<h1>'+TITLE+'</h1>',nuevo,count=1,flags=re.S)
out=pre+nuevo2+post
open('blog/'+slug+'.html','w',encoding='utf-8').write(out)
print('CREADO_'+slug)
