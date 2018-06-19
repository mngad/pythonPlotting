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
        'percent_fill_pc2.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    print(df)
    PC23=df['PC2 +3 ']
    PC22=df['PC2 +2 ']
    PC21=df['PC2 +1 ']
    PC2m=df['Mean ']
    PC2_1=df['PC2 -1 ']
    PC2_2=df['PC2 -2 ']
    PC2_3=df['PC2 -3 ']
    x=df['Specimen']
    plt.plot(x,PC23, label='PC2 +3', marker='.')
    plt.plot(x,PC22, label='PC2 +2', marker='.')
    plt.plot(x,PC21, label='PC2 +1', marker='.')
    plt.plot(x,PC2m, label='Mean', marker='.')
    plt.plot(x,PC2_1, label='PC2 -1', marker='.')
    plt.plot(x,PC2_2, label='PC2 -2', marker='.')
    plt.plot(x,PC2_3, label='PC2 -3', marker='.')
    plt.ylabel('Change in stiffness from non-augmented (%)')
    plt.xlabel('Cement Fill (%)')

    # plt.legend()
    # plt.plot(ax)
    #ax.grid()
    #ax.set_axisbelow(True)
    plt.legend(fontsize=10)

    plt.tight_layout()
    #plt.show()
    plt.savefig('pca_percent_fill_pc2.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

