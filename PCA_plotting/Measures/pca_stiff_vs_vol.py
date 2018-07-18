"""Plots a boxplot from csv data."""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":

    fig, ax = plt.subplots(1, 1)

    #matplotlib.style.use("ggplot")
    matplotlib.rcParams.update({'font.size': 14})
    df_gs = pd.read_csv(
        'pca_stiff.csv',
        header=0,
        sep=',')
    df_stiff = pd.read_csv(
        'pca_vol.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')

    y=df_gs['PC3']
    x=df_stiff['PC3']
    print()
    #x2=df['Disp Percentage Fill']
    #y2=df['Disp Percentage Change in Stiffness']
    dotsize = 50
    plt.scatter(x=x,y=y,color='k',s=dotsize, marker='o', label='PC3')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)),color='k', linestyle=':')
    #plt.plot([2500,7500],[2500,7500], linestyle=':', c='orange', linewidth=1, label='Perfect Agreement')
    plt.ylabel('Stiffness (N/mm)')
    plt.xlabel(r'Vertebral Body Volume (mm$^3$)')

    plt.legend()
    # plt.plot(ax)
    ax.set_axisbelow(True)
    plt.tight_layout()
    #plt.show()
    plt.savefig('pca_stiff_vs_vol_pc3.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

