from PIL import Image, ImageFilter
# BELOW 3 NOT WORKING
# import PIL
# import PIL.Image
# import PIL.ImageFilter
before = Image.open("1.png")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out1.png")
