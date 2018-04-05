"""Plots a boxplot from csv data."""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":

    matplotlib.style.use("ggplot")

    df = pd.read_csv(
        'M:\\All Work\\VP-Set-spreadsheets(not up to date)\\bovine_res.csv',
        header=0,
        sep='\t')

    ax = df.plot.box()
    ax.set_ylim(0, 8500)
    plt.ylabel('Stiffness (N/mm)')
    ax
    plt.show()
