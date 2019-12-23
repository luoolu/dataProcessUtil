# -*- coding: utf-8 -*-
# @Time    : 12/3/19 8:15 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : rgb2gray.py
# @Software: PyCharm

from PIL import Image

img = Image.open('img/label/dy106_1362915.png').convert('L')
img.save('dy106_1362915.png')
