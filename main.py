from PIL import Image, ImageDraw, ImageFont
import os

path_images = 'F:/pillow2/images/'
images = []
canvas = Image.new('RGB', (1600, 600))
image_drawer = ImageDraw.Draw(canvas)

for path in os.listdir(path_images):
    if os.path.isfile(path_images + path):
        images.append(Image.open(path_images + path))

for i, image in enumerate(images):
    image = image.resize((300, 600), Image.ANTIALIAS)
    images[i] = image

    canvas.paste(image, (300 * i, 0))
    image_drawer.text((300 * i + 100, 580), f'ISO:{image.getexif().get(34855)}',
                      font=ImageFont.truetype("arial.ttf", size=22), fill=(25, 255, 0)
                      )

canvas.save(path_images + 'result/img.jpg')
canvas.show()
