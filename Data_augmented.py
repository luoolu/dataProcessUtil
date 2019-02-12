from PIL import Image
import random
import os
import os.path as osp
import glob


# image_Path= 'data/train/*/*.jpg'
#train data augmented
image_Path= '/home/bdai/Downloads/PycharmProjects/ImageClassification/data/train/00002/*.jpg'
#test data augmented
# test_image_Path='/home/bdai/Downloads/PycharmProjects/fossil/data_t555/test*/*.jpg'


#magePath= 'data/test/other.jpg'
my_filename = glob.glob(image_Path)

f = open('all.txt', 'w')
for i in my_filename:
    # k=' '.join([str(j) for j in i])
    f.write(i + "\n")
    print('i: ',i)
f.close()

print('get image file finished!')

for path in my_filename:
    path = osp.join("/home/bdai/Downloads/PycharmProjects/ImageClassification/", '%s' % path)
    print(path)
    img = Image.open(path)
    img.save(path[0:len(path) - 4] + '.jpg')
    img1 = img.transpose(Image.ROTATE_90)
    img1.save(path[0:len(path) - 4] + '_90.jpg')
    img6 = img1.transpose(Image.FLIP_TOP_BOTTOM)
    img6.save(path[0:len(path) - 4] + '_90_TOP_BOTTOM.jpg')
    img7 = img1.transpose(Image.FLIP_LEFT_RIGHT)
    img7.save(path[0:len(path) - 4] + '_90_LEFT_RIGHT.jpg')
    img2 = img.transpose(Image.ROTATE_180)
    img2.save(path[0:len(path) - 4] + '_180.jpg')
    img3 = img.transpose(Image.ROTATE_270)
    img3.save(path[0:len(path) - 4] + '_270.jpg')
    img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img4.save(path[0:len(path) - 4] + '_LEFT_RIGHT.jpg')
    img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img5.save(path[0:len(path) - 4] + '_TOP_BOTTOM.jpg')

print('image augmented finished!')