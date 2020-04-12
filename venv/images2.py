from PIL import Image, ImageFilter

img = Image.open('Astro.jpg')
img.thumbnail((500, 500))
img.save('thumbnail.jpg') 