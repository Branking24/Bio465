import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from processed_data.load_brain_data import load_brain_data


def plot_figures(*argv):

    genes = ["C1orf112", "RAD52", "ENPP4", "LASP1"]

    type = "PBMC"

    omics_df, new_merge, grouped, mean_df, standard, test_df = load_brain_data(
        argv[0])
    var_df = omics_df

    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(15, 7), sharex=False, sharey=True)
    axes = axes.ravel()  # array to 1D
    for gene, ax in zip(genes, axes):
        to_plot = var_df.loc[:, gene]
        to_plot_2 = to_plot[to_plot != 0]
        sns.histplot(data=to_plot_2, kde=False, ax=ax, color=mcolors.CSS4_COLORS["lightsteelblue"])
        ax.axvline(mean_df.loc[gene], color=mcolors.TABLEAU_COLORS["tab:red"])
        ax.axvline(mean_df.loc[gene] - standard.loc[gene], color=mcolors.TABLEAU_COLORS["tab:red"],
                    dashes=[5, 2, 0, 0])
        ax.axvline(mean_df.loc[gene] + standard.loc[gene], color=mcolors.TABLEAU_COLORS["tab:red"],
                    dashes=[5, 2, 0, 0])
        to_plot = var_df.loc[var_df.index == type]
        to_plot_2 = to_plot.loc[:, gene]
        to_plot_3 = to_plot_2[to_plot_2 != 0]
        sns.histplot(data=to_plot_3, kde=False, ax=ax, color=mcolors.TABLEAU_COLORS["tab:orange"])


        # ax.set(title="Single " + col + " Cell", ylabel="Matching Features Count", xlabel="Cell Type Average")
        ax.yaxis.set_tick_params(labelbottom=True)
        fig.tight_layout()
        fig.suptitle("Standard Deviation Classification Method", size=16)
        fig.subplots_adjust(top=0.88)
        plt.savefig("Figure2.png")
    return

plot_figures("data/GSE181153_ADAB_geneCounts.tsv")