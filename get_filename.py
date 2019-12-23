# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 下午3:36
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : get_filename.py
# @Software: PyCharm
import ntpath
import os
# print(os.path.basename("/home/luolu/Downloads/GYST_weather/Test"))
import os

for subdir, dirs, files in os.walk("/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/Habshan/image"):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        # print(file.split(".")[0])
        print(str(file.split("_")[-2]).replace(".", ""))

        # if filepath.endswith(".asm"):
        #     print (filepath)