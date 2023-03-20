import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
# from processed_data.load_cancer_data import load_cancer_data
from processed_data.load_brain_data import load_brain_data


def plot_figures(*argv):
    gene1 = "C1orf112"
    gene2 = "TNMD"
    # TSPAN6, TNMD, DPM1 SCYL3, C1orf112, FGR, CFH
    # omics_df, model_df, new_merge, grouped, mean_df, standard = load_cancer_data(
    #     argv[0], argv[1], "DepmapModelType", "ModelID")
    omics_df, new_merge, grouped, mean_df, standard = load_brain_data(
        argv[0])
    to_plot = omics_df.iloc[:, 4]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"], stat="density")
    plt.axvline(mean_df.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene1] - standard.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene1] + standard.loc[gene1], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    # to_plot = new_merge.loc[new_merge["DepmapModelType"] == "AMLGATA2MECOM"]
    # to_plot_2 = to_plot.iloc[:, 4]
    # to_plot_3 = to_plot_2[to_plot_2 != 0]
    # plot_2 = sns.histplot(data = to_plot_3,kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()
    to_plot = omics_df.iloc[:, 1]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"], stat="density")
    plt.axvline(mean_df.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc[gene2] - standard.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc[gene2] + standard.loc[gene2], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.show()

# plot_figures("OmicsExpressionProteinCodingGenesTPMLogp1.csv", "Model.csv")
plot_figures("../data/GSE181153_ADAB_geneCounts.tsv")