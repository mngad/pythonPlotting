import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns


def bx():

    matplotlib.style.use("ggplot")
    pca_df = pd.read_csv(
        'pcavariables.csv',
        header=0,
        sep=',')

    input_df = pd.read_csv(
        'inputvariables.csv',
        header=0,
        sep=',')
    df = pd.DataFrame()
    df = pd.concat([input_df, pca_df])
    df.reset_index(drop=True,inplace=True)
  #  print(df)
    dd = pd.melt(df,id_vars=['Group'],var_name='Measurements')
    #dd = pd.melt(df,id_vars=['Group'], value_vars=['SLD','SLH','SMD','SMH','SRD','SRH','CAH','CAW','CMH','CMW','CPH','CPW','AID','AIW','AMD','AMW','ASD','ASW'],var_name='Measurements')
    sns.boxplot(x='Measurements', y='value', data=dd, hue='Group')
 #   print(input_df.mean())
#    print(input_df.max())

    plt.show()


def scatter_input_red():

    df = pd.read_csv('input_reduction.csv', header=0, sep=',')
    print(df)
    x=df['Input Number']
    y=df[' Volume Percentage']

    #plt.scatter(x,y)
    plt.plot(x,y, 'ro', markevery=1)
    plt.xlabel('Number of Input Vertebrae')
    plt.ylabel('Percentage of All Input Vertebrae Mean')

    plt.show()

if __name__ == "__main__":
    scatter_input_red()
