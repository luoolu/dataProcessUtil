# -*- coding: utf-8 -*-
# @Time    : 9/3/19 3:44 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : tif2jpg.py
# @Software: PyCharm

import os
from PIL import Image

# yourpath = os.getcwd()
yourpath = "/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/Habshan/image/"
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print("A jpeg file already exists for %s" % name)
            # If a jpeg is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    print("Generating jpeg for %s" % name)
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                except Exception as e:
                    print(e)
