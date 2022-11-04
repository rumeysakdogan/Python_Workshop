"""
Edit your Photos in a Pythonic way by using the below automation script that will let you Photoshop your photos programmatically. This script is handy when you are working on an image processing project or need a hand to edit bulk images like cropping, flipping, enhancing the quality, compressing the size, and much more.

Bulk Photo Editing
Can be used in Projects
much more
"""

# Python Photoshop
# pip install Pillow

from PIL import Image
import PIL


# loading image
im = Image.open("python.png")
# get image info
print(im.format, im.size, im.mode)
# Crop
img = im.crop((0, 0, 100, 100))
img.save("cropped.png")
# Resize
img = im.resize((100, 100), Image.ANTIALIAS)
img.save("resized.png")
# Rotate
img = im.rotate(180)
img.save("rotated.png")
# Flip
img = im.transpose(Image.FLIP_LEFT_RIGHT)
img.save("flip.png")
# Compress size
img.save("python.png", optimize=True, quality=95)
# Greyscale
img = im.convert('L')
img.save("grey.png")
# Enhance image
enhancer = PIL.ImageEnhance.Contrast(im)
enhancer.enhance(1.3)
img.save("enhanced_image.png")
# Blur
img = im.filter(PIL.ImageFilter.BLUR)
img.save("bluring.png")
# Drop shadow Effect
img = im.filter(PIL.ImageFilter.GaussianBlur(2))
img.save("drop_shadow.png")
# Increase brightness
img = im.point(lambda b: b * 1.2)
img.save("bright.png")
# merge two images
img2 = Image.open("python2.png")
img = Image.blend(im, img2, 0.5)
img.save("merge.png")