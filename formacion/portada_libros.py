from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
img = Image.new("RGB", (W, H), (10, 34, 58))  # azul marino #0a2a4a
d = ImageDraw.Draw(img)

# Fondo degradado suave (más claro arriba)
for y in range(H):
    r = 8 + int(y/H*8)
    g = 28 + int(y/H*16)
    b = 48 + int(y/H*30)
    d.line([(0,y),(W,y)], fill=(r,g,b))

# Borde dorado
d.rectangle([20,20,W-20,H-20], outline=(212,175,55), width=6)

FONT_B = "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/montserrat/Montserrat-Regular.ttf"
import os
if not os.path.exists(FONT_B): FONT_B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
if not os.path.exists(FONT_R): FONT_R=FONT_B

# Título
f1 = ImageFont.truetype(FONT_B, 64)
f2 = ImageFont.truetype(FONT_B, 92)
f3 = ImageFont.truetype(FONT_B, 40)
f4 = ImageFont.truetype(FONT_R, 36)

title_lines = ["📚", "LOS 5 LIBROS DE", "FINANZAS QUE", "TODOS DEBERÍAN LEER"]
y = 120
for i, line in enumerate(title_lines):
    if i==0:
        font = ImageFont.truetype(FONT_R, 72)
        color = (255,255,255)
    elif i==1:
        font = f1; color=(255,255,255)
    elif i==2:
        font = f2; color=(212,175,55)  # dorado
    else:
        font = f1; color=(255,255,255)
    bb = d.textbbox((0,0), line, font=font)
    w = bb[2]-bb[0]
    x = (W-w)//2 - bb[0]
    # sombra
    d.text((x+3, y+3), line, font=font, fill=(0,0,0,160))
    d.text((x, y), line, font=font, fill=color)
    y += int(bb[3]-bb[1]) + 15

# Separador dorado
d.rectangle([140, y+10, W-140, y+14], fill=(212,175,55))
y += 45

# Lista de libros
books = ["Padre rico, padre pobre",
         "El hombre más rico de Babilonia",
         "La psicología del dinero",
         "Invierte en ti mismo",
         "El pequeño libro para invertir (Bogle)"]
for b in books:
    d.text((W//2 - 400, y), "💰 ", font=f4, fill=(212,175,55))  
    bb=d.textbbox((0,0), b, font=f3)
    d.text((W//2 - 300, y), b, font=f3, fill=(255,255,255))
    y += 62

# CTA
y += 30
cta = "Empieza HOY tu libertad financiera"
bb=d.textbbox((0,0), cta, font=f4)
w=bb[2]-bb[0]
d.rounded_rectangle([(W-w)//2-30, y-15, (W+w)//2+30, y+52], radius=30, fill=(212,175,55))
d.text(((W-w)//2, y), cta, font=f4, fill=(10,34,58))

img.save("libros_finanzas_portada.png")
print("portada generada")
