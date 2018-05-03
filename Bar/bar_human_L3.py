import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
n_groups = 8
mpl.rcParams.update({'font.size': 16})
df = pd.read_csv(
        'new_data/human_1_2.csv',
        header=0,
        sep=',')
# create plot

VB0 = df['G17-11 L1']
VB1 = df['G17-11 L2']
VB2 = df['G17-11 L3']
VB3 = df['G17-11 L4']
VB4 = df['G17-11 L5']
VB5 = df['G19-11 L1']
VB6 = df['G21-11 L1']
VB7 = df['G21-11 L2']
VB8 = df['G21-11 L3']
VB9 = df['G41-11 L1']
VB10 = df['G41-11 L2']
VB11 = df['G41-11 L3']
VB12 = df['G41-11 L4']
VB13 = df['G41-11 L5']

fig, ax = plt.subplots()
index = np.arange(n_groups)
novb = 3.0
bar_width = 0.8/novb
opacity = 0.8

#rects1 = plt.bar(index, VB0, bar_width,
#                 alpha=opacity,
#                 color='b',
#                 label='Spine 1 L1')
#rects2 = plt.bar(index + (bar_width) , VB1, bar_width,
#                 alpha=opacity,
#                 color='g',
#                 label='Spine 1 L2')
rects3 = plt.bar(index+ (bar_width *0), VB2, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Spine 1 L3')
#rects4 = plt.bar(index + (bar_width *3), VB3, bar_width,
#                 alpha=opacity,
#                 color='c',
#                 label='Spine 1 L4')
#rects5 = plt.bar(index + (bar_width *4), VB4, bar_width,
#                 alpha=opacity,
#                 color='m',
#                 label='Spine 1 L5')
#rects6 = plt.bar(index+ (bar_width), VB5, bar_width,
#                 alpha=opacity,
#                 color='y',
#                 label='Spine 2 L1')
#rects7 = plt.bar(index + (bar_width*2) , VB6, bar_width,
#                 alpha=opacity,
#                 color='k',
#                 label='Spine 3 L1')
#rects8 = plt.bar(index+ (bar_width *7), VB7, bar_width,
#                 alpha=opacity,
#                 color='xkcd:purple',
#                 label='Spine 3 L2')
rects9 = plt.bar(index + (bar_width *1), VB8, bar_width,
                 alpha=opacity,
                 color='xkcd:teal',
                 label='Spine 3 L3')
#rects10 = plt.bar(index + (bar_width *3), VB9, bar_width,
#                 alpha=opacity,
#                 color='xkcd:olive',
#                 label='Spine 4 L1')
#rects11 = plt.bar(index+ (bar_width *10), VB10, bar_width,
#                 alpha=opacity,
#                 color='xkcd:salmon',
#                 label='Spine 4 L2')
rects12 = plt.bar(index + (bar_width*2) , VB11, bar_width,
                 alpha=opacity,
                 color='xkcd:periwinkle',
                 label='Spine 4 L3')
#rects13 = plt.bar(index+ (bar_width *12), VB12, bar_width,
#                 alpha=opacity,
#                 color='xkcd:turquoise',
#                 label='Spine 4 L4')
#rects14 = plt.bar(index + (bar_width *13), VB13, bar_width,
#                 alpha=opacity,
#                 color='xkcd:mustard',
#                 label='Spine 4 L5')

plt.xlabel('Loading Position')
plt.ylabel('Change in Stiffness (%)')
plt.xticks(index + bar_width)
ax.set_xticklabels( df['Position'])
plt.legend(fontsize=10)


plt.tight_layout()
#plt.show()
plt.savefig('hum_L3_1_2.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
