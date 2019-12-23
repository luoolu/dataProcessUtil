# -*- coding: utf-8 -*-
# @Time    : 8/7/19 10:32 AM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : extension_rename.py
# @Software: PyCharm

import os


class BatchRename:
    def __init__(self):
        self.path = '/home/xkjs/Desktop/image/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.JPG'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),  item.replace('JPG', 'jpg'))
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
