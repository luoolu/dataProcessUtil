"""Converts png, bmp and gif to jpg, removes descriptions and resizes the image to a maximum of 1920x1080."""

from PIL import Image
from glob import glob
import PIL
import sys
import os

path = '/home/xkjs/Downloads/data/weather&Cloud/GYST_weather/train_jpg'
path_originals = '/home/xkjs/Downloads/data/weather&Cloud/GYST_weather/Train/'
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

if not os.path.exists(path):
    os.makedirs(path)


def compress_image(image, infile):
    size = 1920, 1080
    width = 1920
    height = 1080
    listing = os.listdir(path_originals)

    name = infile.split('.')
    first_name = path + '/' + name[0] + '.jpg'
    if image.size[0] > width and image.size[1] > height:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(first_name, quality=100)
    elif image.size[0] > width:
        wpercent = (width / float(image.size[0]))
        height = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((width, height), PIL.Image.ANTIALIAS)
        image.save(first_name, quality=100)
    elif image.size[1] > height:
        wpercent = (height / float(image.size[1]))
        width = int((float(image.size[0]) * float(wpercent)))
        image = image.resize((width, height), PIL.Image.ANTIALIAS)
        image.save(first_name, quality=100)
    else:
        image.save(first_name, quality=100)


counter = 0


def processImage():
    global counter
    listing = os.listdir(path_originals)
    for infile in listing:
        img = Image.open(path_originals + infile)
        name = infile.split('.')
        first_name = path + '/' + name[0] + '.jpg'
        print("name: ", name)
        print("img format: ", img.format)
        counter = counter + 1

        if img.format == "JPEG":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()

        elif img.format == "GIF":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()

        elif img.format == "WEBP":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()

        elif img.format == "MPO":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()


        elif img.format == "PNG":
            try:
                image = Image.new("RGB", img.size, (255, 255, 255))
                image.paste(img, img)
                compress_image(image, infile)
            except ValueError:
                image = img.convert('RGB')
                compress_image(image, infile)
            img.close()

        elif img.format == "BMP":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()


processImage()
print("counter: ", counter)
