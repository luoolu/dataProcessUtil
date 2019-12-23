# -*- coding: utf-8 -*-
# @Time    : 10/15/19 5:01 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : png2jpg.py
# @Software: PyCharm
import os

from PIL import Image  # Python Image Library - Image Processing
import glob
import cv2
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# if img.mode == "P":
#         img = img.convert('RGB')

counter = 0
images = glob.glob("/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/DY0106101D Core Data/thin section/Zone G/dyzg_image/*.png")
path = "/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/DY0106101D Core Data/thin section/Zone G/106zg/"
for j in images:
    # print("j:\n", j)
    im = Image.open(j)
    # rgb_im = im.convert("RGB")

    if im.mode == "P":
       im = im.convert('RGB')
       counter = counter + 1
       print("j:\n", j)

    print("j-split:\n", j.split("_")[-1])
    new_name = "106zg_" + j.split("_")[-1]
    new_name = new_name.split(".")[0]
    print("new_name:", new_name)
    # print("j-split:\n", j.split(".")[1])
    # rgb_im.save(j.replace("png", "jpg"))
    im.save(path + new_name + ".jpg")

    counter = counter + 1
print("counter: ", counter)