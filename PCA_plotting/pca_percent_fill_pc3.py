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
        'percent_fill_pc3.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    print(df)
    PC33=df['PC3 +3 ']
    PC32=df['PC3 +2 ']
    PC31=df['PC3 +1 ']
    PC3m=df['Mean ']
    PC3_1=df['PC3 -1 ']
    PC3_2=df['PC3 -2 ']
    PC3_3=df['PC3 -3 ']
    x=df['Specimen']
    plt.plot(x,PC33, label='PC3 +3', marker='.')
    plt.plot(x,PC32, label='PC3 +2', marker='.')
    plt.plot(x,PC31, label='PC3 +1', marker='.')
    plt.plot(x,PC3m, label='Mean', marker='.')
    plt.plot(x,PC3_1, label='PC3 -1', marker='.')
    plt.plot(x,PC3_2, label='PC3 -2', marker='.')
    plt.plot(x,PC3_3, label='PC3 -3', marker='.')
    plt.ylabel('Change in stiffness from non-augmented (%)')
    plt.xlabel('Cement Fill (%)')

    # plt.legend()
    # plt.plot(ax)
    #ax.grid()
    #ax.set_axisbelow(True)
    plt.legend(fontsize=10)

    plt.tight_layout()
    #plt.show()
    plt.savefig('pca_percent_fill_pc3.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

