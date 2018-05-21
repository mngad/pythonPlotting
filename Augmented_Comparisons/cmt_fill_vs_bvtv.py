"""Plots a boxplot from csv data."""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    fig, ax = plt.subplots(1, 1)

    #matplotlib.style.use("ggplot")
    matplotlib.rcParams.update({'font.size': 14})
    df = pd.read_csv(
        'cmt_fill_vs_bvtv.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    
    x1=df['BV/TV']
    y1=df['Percentage Fill']
    #x2=df['Percentage Fill b']
    #y2=df['Percentage Change in Stiffness b']
    #x2=df['Disp Percentage Fill']
    #y2=df['Disp Percentage Change in Stiffness']
    dotsize = 100
    plt.scatter(x=x1,y=y1,color='red',s=dotsize, marker='o', label='Concentrated Cement \n Volume')
    #plt.scatter(x=x2,y=y2,color='blue',s=dotsize, marker='^', label='Dispersed Cement \n Volume')
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)),color='red', linestyle=':')
    # plt.plot(np.unique(x2), np.poly1d(np.polyfit(x2, y2, 1))(np.unique(x2)),color='blue', linestyle=':')
    #plt.plot([2000,7500],[2000,7500], linestyle=':', c='orange', linewidth=1)
    plt.ylabel('Percentage Fill (%)')
    plt.xlabel('Bone Volume Fraction')
 
    # plt.legend()
    # plt.plot(ax)
    ax.grid()
    ax.set_axisbelow(True)
    #plt.legend(fontsize=10)
    plt.text(0.32,45,s='r=0.85', color='red')

    plt.tight_layout()
    #plt.show()
    plt.savefig('cmt_fill_vs_bvtv.png', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

