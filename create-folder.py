# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 下午4:11
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : create-folder.py
# @Software: PyCharm

import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# Example
# Creates a folder in the current directory called data
# createFolder('./data/')

for i in range(9):
    createFolder("/home/xkjs/Downloads/data/weather&Cloud/GYST_weather/train/0000" + str(i) + "/")
