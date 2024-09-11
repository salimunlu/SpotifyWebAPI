import seaborn as sns
import matplotlib.pyplot as plt


def plot_scatter(df):
    ax = sns.scatterplot(data=df, x="valence", y="danceability")
    ax.set(xlabel="Valence (Duygusal Pozitiflik)", ylabel="Danceability (Dans Edilebilirlik)",
           title="Scatterplot")
    plt.show()

