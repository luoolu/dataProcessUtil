# -*- coding: utf-8 -*-
# @Time    : 12/3/19 8:59 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : batch_resize.py
# @Software: PyCharm

# !/usr/bin/python
from PIL import Image
import os, sys

path = "/home/xkjs/PycharmProjects/pre_process/plot_result"
dirs = os.listdir(path)


def resize():
    for item in dirs:
        # print(path + "/" + item)
        if os.path.isfile(path + "/" + item):
            print(path + "/" + item)
            im = Image.open(path + "/" + item)
            f, e = os.path.splitext(path + "/" + item)
            imResize = im.resize((1280, 1024), Image.ANTIALIAS)
            imResize.save(path + "/" + item, 'PNG', quality=100)


resize()
