import re
idx=open('blog/index.html',encoding='utf-8').read()
slug='como-empezar-a-ahorrar-e-invertir'
TITLE='Cómo empezar a ahorrar e invertir desde cero'
# extracto del articulo nuevo (primer parrafo)
contenido=open('blog/'+slug+'.html',encoding='utf-8').read()
mp=re.search(r'<p>(.*?)</p>',contenido,re.S)
extracto=re.sub(r'<[^>]+>','',mp.group(1)).strip()
if len(extracto)>115: extracto=extracto[:112].rstrip()+'...'
FECHA='6 agosto 2026'
tarjeta=('<div class="blog-post">\n'
         '<h3>'+TITLE+'</h3>\n'
         '<p>'+extracto+'</p>\n'
         '<p class="date">'+FECHA+'</p>\n'
         '<a href="'+slug+'.html">Leer más →</a>\n'
         '</div>')
# insertar tras la ultima tarjeta blog-post
posts=list(re.finditer(r'<div class="blog-post">',idx))
if posts:
    # encontrar cierre del ultimo </div> de esa tarjeta
    # metodo: insertar antes del cierre de <main>
    cm=idx.rfind('</main>')
    idx=idx[:cm]+tarjeta+chr(10)+idx[cm:]
    open('blog/index.html','w',encoding='utf-8').write(idx)
    print('INSERTADA')
else:
    print('SIN_POSTS')
