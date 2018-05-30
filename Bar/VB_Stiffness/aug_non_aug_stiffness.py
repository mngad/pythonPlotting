import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
n_groups = 14
mpl.rcParams.update({'font.size': 10})
df = pd.read_csv(
        'aug_non_aug_stiffness.csv',
        header=0,
        sep=',')
# create plot

VB0 = df['Non-augmented']
VB1 = df['Augmented']


fig, ax = plt.subplots()
index = np.arange(n_groups)
novb = 2
bar_width = 0.8/novb
opacity = 0.8

rects1 = plt.bar(index, VB0, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Non-augmented \nStiffness')
rects2 = plt.bar(index + (bar_width) , VB1, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Augmented \nStiffness')


plt.xlabel('Specimen')
plt.ylabel('Stiffness (N/mm)')
plt.xticks(index + bar_width)
ax.set_xticklabels( df['Specimen'],rotation = 45, ha="right")
plt.legend(fontsize=10)

plt.tight_layout()
#plt.show()
plt.savefig('aug_non_aug_stiffness.eps', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
plt.savefig('aug_non_aug_stiffness.png', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)