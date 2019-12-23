# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *  # 支持中文
import matplotlib

mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.use('TkAgg')
names = ['0.001', '0.01', '0.1', '1', '10', '100', '1000']

with open('temp_x.txt') as f:
    x = f.readlines()
with open('temp_y.txt') as f:
    y = f.readlines()

# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
plt.xlim(0.001, 1000)  # 限定横轴的范围
plt.ylim(0, 1)  # 限定纵轴的范围
# plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'Strategy1')
# plt.plot(x, y1, marker='*', ms=10,label=u'Strategy2')
# plt.plot(x, y2, marker='+', ms=10,label=u'Strategy3')

plt.plot(x, y, marker='o', ms=10, label=u'')
# plt.plot(x, y2, marker='+', ms=10, label=u'Prevented')

plt.xticks(x, ('0.001', '0.01', '0.1', '1', '10', '100', '1000'))

plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.25)
plt.xlabel(u"")  # X轴标签
plt.ylabel("")  # Y轴标签
plt.title("")  # 标题
# plt.savefig("bike.png")
plt.show()
