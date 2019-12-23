import os


class BatchRename:
    def __init__(self):
        self.path = '/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/Habshan/TS/Photos/DY-106__Habshan_preliminary/p0474_dy-106/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.tif'):
                print(item)
                print(str(item.split("_")[-2]).replace(".", ""))
                new_item = str(item.split("_")[-2]).replace(".", "")
                # new_name = str(item.split("_")[-1])
                # print(new_name)
                src = os.path.join(os.path.abspath(self.path), item)
                if i < 1000:
                    dst = os.path.join(os.path.abspath(self.path), '106hbs_' + new_item)

                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d images' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
