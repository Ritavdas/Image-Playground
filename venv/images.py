from PIL import Image, ImageFilter

img = Image.open('./Pokedex/Pikachu.jpg')
# filtered_img = img.filter(ImageFilter.CONTOUR)
filtered_img = img.convert('L')
# crooked = filtered_img.rotate(180)
# crooked.save("grey.png", 'png')

# resize = filtered_img.resize((500, 500))
# resize.save("grey.png", 'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", 'png')
