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
        'exp_50_yield.csv',
        header=0,
        sep=',')
    
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    
    x1=df['exp']
    y1=df['50_perc']
    
    y2=df['yield']
    y3=df['tied']
    #x2=df['Disp Percentage Fill']
    #y2=df['Disp Percentage Change in Stiffness']
    dotsize = 50
    plt.scatter(x=x1,y=y3,color='C3',s=dotsize, marker='^', label='Tied Interaction')
    plt.scatter(x=x1,y=y1,color='C1',s=dotsize, marker='o', label='Reduced Modulus Interaction')
    plt.scatter(x=x1,y=y2,color='C2',s=dotsize, marker='^', label='Yielding & Reduced Modulus Interaction')
    
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y1, 1))(np.unique(x1)),color='C1', linestyle=':')
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y2, 1))(np.unique(x1)),color='C2', linestyle=':')
    plt.plot(np.unique(x1), np.poly1d(np.polyfit(x1, y3, 1))(np.unique(x1)),color='C3', linestyle=':')
    plt.plot([2500,7500],[2500,7500], linestyle=':', c='C4', linewidth=1, label='Perfect Agreement')
    plt.ylabel('Computational Stiffness (N/mm)')
    plt.xlabel('Experimental Stiffness (N/mm))')
 
    # plt.legend()
    # plt.plot(ax)
    ax.grid()
    ax.set_axisbelow(True)
    plt.legend(fontsize=10)
    plt.text(6000,5500,s='CCC=0.14', color='C3')
    plt.text(6000,5000,s='CCC=0.18', color='C1')
    plt.text(6000,4500,s='CCC=0.23', color='C2')
    
    plt.tight_layout()
    #plt.show()
    plt.savefig('exp_50_yield_tied1121.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

