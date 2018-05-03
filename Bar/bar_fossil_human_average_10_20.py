import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
n_groups = 8
mpl.rcParams.update({'font.size': 16})
df = pd.read_csv(
        'new_data/fossil_10_20.csv',
        header=0,
        sep=',')
df2 = pd.read_csv(
        'new_data/human_10_20.csv',
        header=0,
        sep=',')
# create plot

VB0 = df['Mean']
VB1 = df2['Mean']
fig, ax = plt.subplots()
index = np.arange(n_groups)
novb = 2.0
bar_width = 0.8/novb
opacity = 0.8

rects1 = plt.bar(index, VB0, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Fossil - Mean')
rects2 = plt.bar(index + (bar_width) , VB1, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Human - Mean')
#rects3 = plt.bar(index+ (bar_width *2), VB2, bar_width,
#                 alpha=opacity,
#                 color='r',
#                 label='Spine 1 L3')
#rects4 = plt.bar(index + (bar_width *3), VB3, bar_width,
#                 alpha=opacity,
#                 color='c',
#                 label='Spine 1 L4')
#rects5 = plt.bar(index + (bar_width *4), VB4, bar_width,
#                 alpha=opacity,
#                 color='m',
#                 label='Spine 1 L5')
#rects6 = plt.bar(index+ (bar_width *5), VB5, bar_width,
#                 alpha=opacity,
#                 color='y',
#                 label='Spine 2 L1')
#rects7 = plt.bar(index + (bar_width*6) , VB6, bar_width,
#                 alpha=opacity,
#                 color='k',
#                 label='Spine 3 L1')
#rects8 = plt.bar(index+ (bar_width *7), VB7, bar_width,
#                 alpha=opacity,
#                 color='xkcd:purple',
#                 label='Spine 3 L2')
#rects9 = plt.bar(index + (bar_width *8), VB8, bar_width,
#                 alpha=opacity,
#                 color='xkcd:teal',
#                 label='Spine 3 L3')
#rects10 = plt.bar(index + (bar_width *9), VB9, bar_width,
#                 alpha=opacity,
#                 color='xkcd:olive',
#                 label='Spine 4 L1')
#rects11 = plt.bar(index+ (bar_width *10), VB10, bar_width,
#                 alpha=opacity,
#                 color='xkcd:salmon',
#                 label='Spine 4 L2')
#rects12 = plt.bar(index + (bar_width*11) , VB11, bar_width,
#                 alpha=opacity,
#                 color='xkcd:periwinkle',
#                 label='Spine 4 L3')
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
plt.savefig('hum_10_20.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
