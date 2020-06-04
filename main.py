from PIL import Image, ImageDraw, ImageFont

image = Image.open(f'images/img.png').convert('RGBA')
qr = Image.open('images/qr.png').convert('RGBA')
logo = Image.open('images/logo.png').convert('RGBA')
out = 'F:/pillow1/images/out/img.png'
im_width = 1000

assert im_width >= 480, RuntimeError("Small size")
im_height = im_width * image.size[1] // image.size[0]
image = image.resize((im_width, im_height), Image.ANTIALIAS)

lo_width = im_width // 10
lo_height = lo_width * logo.size[1] // logo.size[0]
logo = logo.resize((lo_width, lo_height), Image.ANTIALIAS)

qr = qr.resize((100, 100), Image.ANTIALIAS)

if image.size[1] > image.size[0]:
    image = image.rotate(180)

draw = ImageDraw.Draw(image)
date = image.getexif().get(36868).split()[0]
text = "Тони Толстячок"
font = ImageFont.truetype("arial.ttf", size=24)
draw.text((im_width // 2 - 125, im_height - 25), f"{text} {date}", font=font)

image.paste(logo, (im_width - lo_width, 0), logo)
image.paste(qr, (0, 0))
image.save(out)
