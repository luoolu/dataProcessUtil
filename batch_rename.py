import os


class BatchRename:
    def __init__(self):
        self.path = '/home/xkjs/PycharmProjects/pre_process/plot_result/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.__contains__("'"):
                # print(item)
                print(str(item.replace("'", "")))
                new_item = str(item.replace("'", ""))
                src = os.path.join(os.path.abspath(self.path), item)
                if i < 1000:
                    dst = os.path.join(os.path.abspath(self.path), new_item)

                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename %d images' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
