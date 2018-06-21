"""Plots a boxplot from csv data."""
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color='k')
    plt.setp(bp['fliers'], color=color)

if __name__ == "__main__":

    fig, ax = plt.subplots(1, 1)

    #matplotlib.style.use("ggplot")
    matplotlib.rcParams.update({'font.size': 14})
    df = pd.read_csv(
        'input.csv',
        header=0,
        sep=',')
    df2 = pd.read_csv(
        'output.csv',
        header=0,
        sep=',')
    #df2 = pd.read_csv(
    #    'M:\Git_Repos\pythonPlotting\Aug_best.csv',
    #    header=0,
    #    sep=',')
    print(df)
    dfdata=[df['SLD'], df['SLH'], df['SMD'], df['SMH'], df['SRD'], df['SRH'], df['CAH'], df['CAW'], df['CMH'], df['CMW'], df['CPH'], df['CPW'], df['AID'], df['AIW'], df['AMD'], df['AMW'], df['ASD'], df['ASW']]
    df2data=[df2['SLD'], df2['SLH'], df2['SMD'], df2['SMH'], df2['SRD'], df2['SRH'], df2['CAH'], df2['CAW'], df2['CMH'], df2['CMW'], df2['CPH'], df2['CPW'], df2['AID'], df2['AIW'], df2['AMD'], df2['AMW'], df2['ASD'], df2['ASW']]
    bpl = plt.boxplot(dfdata,positions=np.array(range(len(dfdata)))*2.0-0.4, widths=0.6, patch_artist=True)
    bpr = plt.boxplot(df2data,positions=np.array(range(len(df2data)))*2.0+0.4, sym='', widths=0.6, patch_artist=True)

    set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
    set_box_color(bpr, '#2C7BB6')
    plt.ylabel('Length of Measurement (mm)')
    #plt.xlabel('Cement Fill (%)')
    ticks = ['SLD', 'SLH', 'SMD', 'SMH', 'SRD', 'SRH', 'CAH', 'CAW', 'CMH', 'CMW', 'CPH', 'CPW', 'AID', 'AIW', 'AMD', 'AMW', 'ASD', 'ASW']
    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    # plt.legend()
    # plt.plot(ax)
    #ax.grid()
    #ax.set_axisbelow(True)
    #plt.legend(fontsize=10)

    #plt.tight_layout()
    #plt.show()
    plt.savefig('pca_cube.pdf', dpi=320, facecolor='w', edgecolor='w',
        orientation='landscape', papertype='a4', format=None,
        transparent=False, bbox_inches=None, pad_inches=1,
        frameon=None)

