import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from processed_data.load_cancer_data import load_cancer_data


def plot_figures(*argv):
    omics_df, model_df, new_merge, grouped, mean_df, standard = load_cancer_data(
        argv[0], argv[1], "DepmapModelType", "ModelID")
    to_plot = omics_df.iloc[:, 4]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc["SCYL3 (57147)"], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc["SCYL3 (57147)"] - standard.loc["SCYL3 (57147)"], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc["SCYL3 (57147)"] + standard.loc["SCYL3 (57147)"], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    to_plot = new_merge.loc[new_merge["DepmapModelType"] == "AMLGATA2MECOM"]
    to_plot_2 = to_plot.iloc[:, 4]
    to_plot_3 = to_plot_2[to_plot_2 != 0]
    plot_2 = sns.histplot(data = to_plot_3,kde=False, color=mcolors.CSS4_COLORS["moccasin"])
    plt.show()
    to_plot = omics_df.iloc[:, 3]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True, color=mcolors.CSS4_COLORS["lightsteelblue"])
    plt.axvline(mean_df.loc["DPM1 (8813)"], color=mcolors.TABLEAU_COLORS["tab:red"])
    plt.axvline(mean_df.loc["DPM1 (8813)"] - standard.loc["DPM1 (8813)"], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.axvline(mean_df.loc["DPM1 (8813)"] + standard.loc["DPM1 (8813)"], color=mcolors.TABLEAU_COLORS["tab:red"], dashes=[5, 2, 0, 0])
    plt.show()

plot_figures("OmicsExpressionProteinCodingGenesTPMLogp1.csv", "Model.csv")