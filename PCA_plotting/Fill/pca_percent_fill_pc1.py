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
        'percent_fill_pc1.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    print(df)
    PC13=df['PC1 +3 ']
    PC12=df['PC1 +2 ']
    PC11=df['PC1 +1 ']
    PC1m=df['Mean ']
    PC1_1=df['PC1 -1 ']
    PC1_2=df['PC1 -2 ']
    PC1_3=df['PC1 -3 ']
    x=df['Specimen']
    plt.plot(x,PC13, label='PC1 +3', marker='.')
    plt.plot(x,PC12, label='PC1 +2', marker='.')
    plt.plot(x,PC11, label='PC1 +1', marker='.')
    plt.plot(x,PC1m, label='Mean', marker='.')
    plt.plot(x,PC1_1, label='PC1 -1', marker='.')
    plt.plot(x,PC1_2, label='PC1 -2', marker='.')
    plt.plot(x,PC1_3, label='PC1 -3', marker='.')
    plt.ylabel('Change in stiffness from non-augmented (%)')
    plt.xlabel('Cement Fill (%)')

    # plt.legend()
    # plt.plot(ax)
    #ax.grid()
    #ax.set_axisbelow(True)
    plt.legend(fontsize=10)

    plt.tight_layout()
    #plt.show()
    plt.savefig('pca_percent_fill_pc1.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

