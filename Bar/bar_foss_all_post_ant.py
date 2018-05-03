import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
n_groups = 8
mpl.rcParams.update({'font.size': 16})
df = pd.read_csv(
        'new_data/fossil_all_post_ant.csv',
        header=0,
        sep=',')
# create plot
VB0 = df['STS14E']
VB1 = df['STS14F']
VB2 = df['STS14G']
VB3 = df['STS14H']
VB4 = df['STS14I']

fig, ax = plt.subplots()
index = np.arange(n_groups)
novb = 5.0
bar_width = 0.8/novb
print(bar_width)
opacity = 0.8

rects1 = plt.bar(index, VB0, bar_width,
                 alpha=opacity,
                 color='b',
                 label='E')

rects2 = plt.bar(index + (bar_width) , VB1, bar_width,
                 alpha=opacity,
                 color='g',
                 label='F')
rects3 = plt.bar(index+ (bar_width *2), VB2, bar_width,
                 alpha=opacity,
                 color='r',
                 label='G')
rects4 = plt.bar(index + (bar_width *3), VB3, bar_width,
                 alpha=opacity,
                 color='c',
                 label='H')
rects5 = plt.bar(index + (bar_width *4), VB4, bar_width,
                 alpha=opacity,
                 color='m',
                 label='I')

plt.xlabel('Loading Position Distance from Centre \n (Posterior to Anterior, mm)')
plt.ylabel('Change in Stiffness (%)')
plt.xticks(index + bar_width)
ax.set_xticklabels( df['Position'])
plt.legend(fontsize=6)

plt.tight_layout()
#plt.show()
plt.savefig('foss_all_post_ant.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
