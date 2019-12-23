# -*- coding: utf-8 -*-
# @Time    : 10/26/19 6:53 PM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : split_data_folders.py
# @Software: PyCharm

import split_folders

# Split with a ratio.
# To only split into training and validation set,
# set a tuple to `ratio`, i.e, `(.8, .2)`.
split_folders.ratio('/home/xkjs/Downloads/bdai/PycharmProjects/DataUtils/img/image/',
                    output="/home/xkjs/PycharmProjects/Semantic-Segmentation-Suite/Dataset_bp",
                    seed=1337,
                    ratio=(.8, .1, .1))  # default values

# Split val/test with a fixed number of items e.g.
# 100 for each set.
# To only split into training and validation set,
# use a single number to `fixed`, i.e., `10`.

# split_folders.fixed('input_folder',
#                     output="output",
#                     seed=1337,
#                     fixed=(100, 100),
#                     oversample=False)  # default values
