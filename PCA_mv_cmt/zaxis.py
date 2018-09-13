import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
mpl.rcParams.update({'font.size': 10})
df = pd.read_csv(
        'zaxis.csv',
        header=0,
        sep=',')
# create plot


stiffness = df['Stiffness']

ind1 = np.arange(4)

fig, ax = plt.subplots()
bar_width=1
rects1 = plt.bar(ind1, stiffness,
                 color='C1',
                 label='Principal Component 1')


plt.xlabel('Cement Position (mm, inferior to superior)')
plt.ylabel('Stiffness (N/mm)')

plt.xticks(ind1, range(0,len(stiffness)*2,2))
#plt.legend(fontsize=10)
ax.set_ylim([4250,4450])
plt.tight_layout()
#plt.show()
plt.savefig('zaxis_mv_cmt.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
