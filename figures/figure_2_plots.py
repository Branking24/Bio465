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

    type = "PBMC"

    omics_df, new_merge, grouped, mean_df, standard = load_brain_data(
        argv[0])
    var_df = omics_df

    to_plot = var_df.loc[:, gene1]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene1] - standard.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene1] + standard.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene1]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3,kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene2]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene2] - standard.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene2] + standard.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene2]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene3]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene3], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene3] - standard.loc[gene3], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene3] + standard.loc[gene3], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene3]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene4]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene4], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene4] - standard.loc[gene4], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene4] + standard.loc[gene4], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene4]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene5]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene5], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene5] - standard.loc[gene5], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene5] + standard.loc[gene5], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene5]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene6]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene6], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene6] - standard.loc[gene6], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene6] + standard.loc[gene6], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene6]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene7]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene7], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene7] - standard.loc[gene7], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene7] + standard.loc[gene7], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene7]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

    to_plot = var_df.loc[:, gene8]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc[gene8], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene8] - standard.loc[gene8], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene8] + standard.loc[gene8], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = var_df.loc[var_df.index == type]
    to_plot_2 = to_plot.loc[:, gene8]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data=to_plot_3, kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()

plot_figures("data/GSE181153_ADAB_geneCounts.tsv")