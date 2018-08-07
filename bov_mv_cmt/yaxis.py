import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
mpl.rcParams.update({'font.size': 10})
df = pd.read_csv(
        'yaxis.csv',
        header=0,
        sep=',')
# create plot


stiffness = df['Stiffness']

ind1 = np.arange(len(stiffness))

fig, ax = plt.subplots()
bar_width=1
rects1 = plt.bar(ind1, stiffness,
                 color='C1',
                 label='Principal Component 1')


plt.xlabel('Cement Position (mm)')
plt.ylabel('Stiffness (N/mm)')

plt.xticks(ind1, range(0,len(stiffness)*2,2))
#plt.legend(fontsize=10)
ax.set_ylim([4850,4925])
plt.tight_layout()
#plt.show()
plt.savefig('yaxis_mv_cmt.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
