import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
mpl.rcParams.update({'font.size': 10})
df = pd.read_csv(
        'pca_gs.csv',
        header=0,
        sep=',')
# create plot

PC1 = df['PC1']
PC2 = df['PC2']
PC3 = df['PC3']
ind1 = np.arange(7)
ind2 = np.arange(7, 14)
ind3 = np.arange(14, 21)
fig, ax = plt.subplots()
bar_width=1
rects1 = plt.bar(ind1, PC1,
                 color='b',
                 label='Principal Component 1')
rects2 = plt.bar(ind2, PC2,
                 color='g',
                 label='Principal Component 2')
rects3 = plt.bar(ind3, PC3,
                 color='r',
                 label='Principal Component 3')

plt.xlabel('Model (Standard Deviation)')
plt.ylabel('Mean Greyscale Value')
plt.xticks(np.arange(21))
ax.set_xticklabels( pd.concat([df['Model'],df['Model'],df['Model']]))
plt.legend(fontsize=10)

plt.tight_layout()
#plt.show()
plt.savefig('pca_gs.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
