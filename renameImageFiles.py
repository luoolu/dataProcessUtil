import os
 
class BatchRename():
 def __init__(self):
  self.path = '/home/bdai/Downloads/Data/fossilData/fossil6class/Triangulodus proteus'
 
 def rename(self):
  filelist = os.listdir(self.path)
  total_num = len(filelist)
  i = 0
  for item in filelist:
   if item.endswith('.jpg'):
    src = os.path.join(os.path.abspath(self.path), item)
    if i < 10:
     dst = os.path.join(os.path.abspath(self.path), '03372_0000' + str(i) + '.jpg')
    else:
     dst = os.path.join(os.path.abspath(self.path), '03372_000' + str(i) + '.jpg')
    try:
     os.rename(src, dst)
     print ('converting %s to %s ...' % (src, dst))
     i = i + 1
    except:
     continue
  print ('total %d to rename & converted %d jpgs' % (total_num, i))
 
if __name__ == '__main__':
 demo = BatchRename()
 demo.rename()