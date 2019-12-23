# coding: utf-8
from array import array

from PIL import Image, ImageDraw
import os
import os.path
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 指明被遍历的文件夹
rootdir = r'img'
for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        img = Image.open(currentPath)
        print(img.format, img.size, img.mode)
        # img.show()
        h, w = img.size
        box1 = (0, 420, h, w)  # 设置左、上、右、下的像素
        # image1 = img.crop(box1)  # 图像裁剪

        #
        draw = ImageDraw.Draw(img)
        draw.rectangle([850, 2150, 1050, 4000], fill='black')
        draw.rectangle([1600, 2150, 1800, 4000], fill='black')
        draw.rectangle([2350, 2150, 2550, 4000], fill='black')
        draw.rectangle([3200, 2150, 3400, 4000], fill='black')
        draw.rectangle([3950, 2150, 4150, 4000], fill='black')

        img.save(r"out/" + filename)  # 存储裁剪得到的图像
