# -*- coding: utf-8 -*-
# @Time    : 12/3/19 6:37 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : tif2png.py
# @Software: PyCharm
import os

from PIL import Image
from PIL import ImageSequence
from pathlib import Path

renamed_dir = "/home/xkjs/PycharmProjects/pre_process/bp_png/"
def tif_to_png(path):
    '''
    Converte arquivo .tif para png splitando as páginas do documento.
    | Parâmetros:
    |-- path: Caminho do arquivo.
    '''
    im = Image.open(path)
    name = str(Path(path).parent) + "/" + str(Path(path).stem)
    print("name:", name)
    for i, page in enumerate(ImageSequence.Iterator(im)):
        # page.save(name + "_%d.png" % i, quality=300)
        # print(name + ".png")
        # print(name.split('_')[-2].replace(".", ""))
        new_name = name.split('/')[-1]
        print("new_name:", new_name)
        page.save(renamed_dir + "106hbs_" + new_name + ".png", quality=300)


for subdir, dirs, files in os.walk("/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/Habshan/TS/Photos/DY-106__Habshan_preliminary/p0474_dy-106"):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        print(filepath)
        tif_to_png(filepath)
