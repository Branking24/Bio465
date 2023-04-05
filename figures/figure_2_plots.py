import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
# from processed_data.load_cancer_data import load_cancer_data
from processed_data.load_brain_data import load_brain_data


def plot_figures(*argv):
    gene1 = "C1orf112"
    gene2 = "FGR"
    gene3 = "LASP1"
    gene4 = "KLHL13"
    gene5 = "SNX11"
    gene6 = "TMEM176A"
    gene7 = "CASP10"
    gene8 = "CFLAR"

    genes = ["C1orf112", "FGR", "LASP1", "KLHL13", "SNX11", "TMEM176A", "CASP10", "CFLAR"]

    type = "PBMC"

    omics_df, new_merge, grouped, mean_df, standard, test_df = load_brain_data(
        argv[0])
    var_df = omics_df

    # to_plot = var_df.loc[:, gene1]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene1] - standard.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene1] + standard.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene1]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3,kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene2]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene2] - standard.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene2] + standard.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene2]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene3]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene3], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene3] - standard.loc[gene3], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene3] + standard.loc[gene3], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene3]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene4]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene4], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene4] - standard.loc[gene4], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene4] + standard.loc[gene4], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene4]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene5]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene5], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene5] - standard.loc[gene5], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene5] + standard.loc[gene5], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene5]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene6]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene6], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene6] - standard.loc[gene6], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene6] + standard.loc[gene6], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene6]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene7]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene7], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene7] - standard.loc[gene7], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene7] + standard.loc[gene7], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene7]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()
    #
    # to_plot = var_df.loc[:, gene8]
    # to_plot_2 = to_plot[to_plot != 0]
    # plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    # plt.axvline(mean_df.loc[gene8], color=mcolors.TABLEAU_COLORS["tab:red"])
    # plt.axvline(mean_df.loc[gene8] - standard.loc[gene8], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # plt.axvline(mean_df.loc[gene8] + standard.loc[gene8], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = var_df.loc[var_df.index == type]
    # to_plot_2 = to_plot.loc[:, gene8]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    # plt.show()

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(15, 7), sharex=False, sharey=True)
    axes = axes.ravel()  # array to 1D
    for gene, ax in zip(genes, axes):
        to_plot = var_df.loc[:, gene]
        to_plot_2 = to_plot[to_plot != 0]
        sns.histplot(data=to_plot_2, kde=True, ax=ax, color=mcolors.CSS4_COLORS["lightsteelblue"])
        ax.axvline(mean_df.loc[gene], color=mcolors.TABLEAU_COLORS["tab:red"])
        ax.axvline(mean_df.loc[gene] - standard.loc[gene], color=mcolors.TABLEAU_COLORS["tab:red"],
                    dashes=[5, 2, 0, 0])
        ax.axvline(mean_df.loc[gene] + standard.loc[gene], color=mcolors.TABLEAU_COLORS["tab:red"],
                    dashes=[5, 2, 0, 0])
        to_plot = var_df.loc[var_df.index == type]
        to_plot_2 = to_plot.loc[:, gene]
        to_plot_3 = to_plot_2[to_plot_2 != 0]
        sns.histplot(data=to_plot_3, kde=False, ax=ax, color=mcolors.TABLEAU_COLORS["tab:purple"])


        # ax.set(title="Single " + col + " Cell", ylabel="Matching Features Count", xlabel="Cell Type Average")
        ax.yaxis.set_tick_params(labelbottom=True)
        fig.tight_layout()
        fig.suptitle("Standard Deviation Classification Method", size=16)
        fig.subplots_adjust(top=0.88)
        plt.savefig("Figure2.png")
    return

plot_figures("../data/GSE181153_ADAB_geneCounts.tsv")