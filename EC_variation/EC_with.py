import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# data to plot
n_groups = 6
mpl.rcParams.update({'font.size': 7})
df = pd.read_csv(
        'with_inf.csv',
        header=0,
        sep=',')
df2 = pd.read_csv(
        'with_sup.csv',
        header=0,
        sep=',')
df3 = pd.read_csv(
        'with_both.csv',
        header=0,
        sep=',')
# create plot

inf1=df['Spine 1 L2 Change']
inf2=df['Spine 4 L5 Change']
sup1=df2['Spine 1 L2 Change']
sup2=df2['Spine 4 L5 Change']
both1=df3['Spine 1 L2 Change']
both2=df3['Spine 4 L5 Change']
fig, axarr = plt.subplots(3)
index = np.arange(n_groups)
novb = 2.0
bar_width = 0.8/novb
opacity = 0.8

rects1 = axarr[0].bar(index, inf1, bar_width,
                 alpha=opacity,
                 color='C1',
                 label='Spine 1, L2')
rects2 = axarr[0].bar(index + (bar_width) , inf2, bar_width,
                 alpha=opacity,
                 color='C2',
                 label='Spine 4, L5')
axarr[0].set_xticks(index+ bar_width/2)
axarr[0].set_xticklabels( df['Type'])

rects3 = axarr[1].bar(index, sup1, bar_width,
                 alpha=opacity,
                 color='C1')
rects4 = axarr[1].bar(index + (bar_width) , sup2, bar_width,
                 alpha=opacity,
                 color='C2')
axarr[1].set_xticks(index+ bar_width/2)
axarr[1].set_xticklabels( df2['Type'])

rects1 = axarr[2].bar(index, both1, bar_width,
                 alpha=opacity,
                 color='C1')
rects2 = axarr[2].bar(index + (bar_width) , both2, bar_width,
                 alpha=opacity,
                 color='C2')
axarr[2].set_xticks(index + bar_width/2)
axarr[2].set_xticklabels( df3['Type'])


#axarr[0].set_title(r'Non-Augmented')

#axarr[0].set(ylabel='PC1')
#axarr[1].set(ylabel='PC2')
#axarr[2].set(ylabel='PC3')
plt.tight_layout()
for ax in axarr.flat:
    ax.grid(color='C7', linestyle=':', linewidth=0.5)
    ax.set_axisbelow(True)
    ax.set_ylabel('Change in Stiffness (%)')
#fig.subplots_adjust(hspace=0,wspace=0)


#fig.text(0.007, 0.5, 'Change in Stiffness (%)', ha='center', va='center', rotation='vertical')
# plt.xlabel('Loading Position')


axarr[0].legend()

plt.tight_layout()
#plt.show()
plt.savefig('with.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)
