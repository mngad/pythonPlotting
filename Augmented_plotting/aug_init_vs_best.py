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
        'Aug_normal.csv',
        header=0,
        sep=',')
    df_best = pd.read_csv(
        'Aug_best.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    
    x1=df['Experimental']
    y1=df['Computational']
    x2=df_best['Experimental']
    y2=df_best['Computational']
    #x2=df['Disp Percentage Fill']
    #y2=df['Disp Percentage Change in Stiffness']
    dotsize = 50
    plt.scatter(x=x1,y=y1,color='red',s=dotsize, marker='o', label='Initial Method')
    plt.scatter(x=x2,y=y2,color='blue',s=dotsize, marker='^', label='Registation Method')
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)),color='red', linestyle=':')
    plt.plot(np.unique(x2), np.poly1d(np.polyfit(x2, y2, 1))(np.unique(x2)),color='blue', linestyle=':')
    plt.plot([2500,7500],[2500,7500], linestyle=':', c='orange', linewidth=1, label='Perfect Agreement')
    plt.ylabel('Computational Stiffness (N/mm)')
    plt.xlabel('Experimental Stiffness (N/mm))')
 
    # plt.legend()
    # plt.plot(ax)
    ax.grid()
    ax.set_axisbelow(True)
    plt.legend(fontsize=10)
    plt.text(5500,2500,s='CCC=0.18', color='red')
    
    plt.text(2500,6200,s='CCC=0.46', color='blue')
    plt.tight_layout()
    #plt.show()
    plt.savefig('aug_init_vs_best.eps', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

