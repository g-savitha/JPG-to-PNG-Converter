from PIL import Image,ImageFilter,ImageOps

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
grey_img = img.convert('L')
mirrored = ImageOps.mirror(img)

print(img.format)
mirrored.save('mirror.png','png')
grey_img.save('grey.png','png')
filtered_img.save('blur_pikachu.png','png')
filtered_img.show()
rotate = filtered_img.rotate(180)
rotate.save('upside-down.png','png')
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save('crop.png','png')