import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.lines as mlines


mpl.rcParams.update({'font.size': 7})
mpl.rcParams['axes.linewidth'] = 0.7 #set the value globally
df = pd.read_csv(
        'pc1_20.csv',
        header=0,
        sep=',')
dfT=df.set_index('Specimen').T

df2 = pd.read_csv(
        'pc1_35.csv',
        header=0,
        sep=',')
dfT2=df2.set_index('Specimen').T

df3 = pd.read_csv(
        'pc1_50.csv',
        header=0,
        sep=',')
dfT3=df3.set_index('Specimen').T

df4 = pd.read_csv(
        'pc2_20.csv',
        header=0,
        sep=',')
dfT4=df4.set_index('Specimen').T

df5 = pd.read_csv(
        'pc2_35.csv',
        header=0,
        sep=',')
dfT5=df5.set_index('Specimen').T

df6 = pd.read_csv(
        'pc2_50.csv',
        header=0,
        sep=',')
dfT6=df6.set_index('Specimen').T

df7 = pd.read_csv(
        'pc3_20.csv',
        header=0,
        sep=',')
dfT7=df7.set_index('Specimen').T

df8 = pd.read_csv(
        'pc3_35.csv',
        header=0,
        sep=',')
dfT8=df8.set_index('Specimen').T

df9 = pd.read_csv(
        'pc3_50.csv',
        header=0,
        sep=',')
dfT9=df9.set_index('Specimen').T




fig, axarr = plt.subplots(3,3,sharex=True, sharey='row')

axarr[0,0].plot(dfT)
axarr[0,1].plot(dfT2)
axarr[0,2].plot(dfT3)
axarr[1,0].plot(dfT4)
axarr[1,1].plot(dfT5)
axarr[1,2].plot(dfT6)
axarr[2,0].plot(dfT7)
axarr[2,1].plot(dfT8)
axarr[2,2].plot(dfT9)

axarr[0,0].set_title(r'20 % Fill')
axarr[0,1].set_title(r'35 % Fill')
axarr[0,2].set_title(r'50 % Fill')
axarr[0,0].set(ylabel='PC1')
axarr[1,0].set(ylabel='PC2')
axarr[2,0].set(ylabel='PC3')
plt.tight_layout()
for ax in axarr.flat:
    ax.label_outer()
    ax.grid(color='C7', linestyle=':', linewidth=0.5)
fig.subplots_adjust(hspace=0,wspace=0)
fig.text(0.01, 0.5, 'Change in Stiffness (%)', ha='center', va='center', rotation='vertical')
fig.text(0.5, 0.01, 'Position', ha='center', va='center')

blue_line = mlines.Line2D([], [],label='+3',color='C0')
blue_line1 = mlines.Line2D([], [],label='+2',color='C1')
blue_line2 = mlines.Line2D([], [],label='+1',color='C2')
blue_line3 = mlines.Line2D([], [],label='Mean',color='C3')
blue_line4 = mlines.Line2D([], [],label='-1',color='C4')
blue_line5 = mlines.Line2D([], [],label='-2',color='C5')
blue_line6 = mlines.Line2D([], [],label='-3',color='C6')


fig.legend(handles=[blue_line,blue_line1,blue_line2,blue_line3,blue_line4,blue_line5,blue_line6], bbox_to_anchor=(1.1,0.97))

#plt.show()

plt.savefig('AP_change_from_non_aug.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None)