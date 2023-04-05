from comparisons.create_brain_matrices import create_brain_matrices
from comparisons.compare_datasets import compare_dataset
from processed_data.load_brain_data import load_brain_data
from processed_data.load_primary_tissue_data import load_primary_tissue_data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors
import numpy as np



def figure_4_plots():
    infile = "../data/primary_brain_data.csv"
    test_infile = "../data/GSE181153_ADAB_geneCounts.tsv"
    data_transpose, new_merge, grouped, mean_df, standard_df, test_df = load_primary_tissue_data(infile, test_infile)

    new_merge_test = test_df.replace(0, np.nan)  # data normalization --> getting rid of 0s
    grouped_test = new_merge_test.groupby(level=0).mean()
    mean_df_test = grouped_test.mean()
    standard_df_test = new_merge_test.std()

    matrices, sorted_indeces = create_brain_matrices(data_transpose, new_merge, grouped, mean_df, standard_df)
    final, figure_vals = compare_dataset(test_df, standard_df_test, mean_df_test, matrices, sorted_indeces)

    figure_df = pd.DataFrame(figure_vals)

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 7), sharex=False, sharey=True)
    axes = axes.ravel()  # array to 1D
    cols = ['iPSC', 'iMGL', 'HMC3', 'U87a', 'THP1', 'iHPC']
    for col, ax in zip(cols, axes):
        data = figure_df[col]  # select the data
        max_val = max(figure_vals[col][1])
        colors = [mcolors.TABLEAU_COLORS["tab:red"] if y == max_val else mcolors.CSS4_COLORS["lightsteelblue"] for y in figure_vals[col][1]]
        x_vals = figure_vals[col][0]
        sns.barplot(data=data, x=x_vals, y=figure_vals[col][1], ax=ax, palette=colors)
        ax.set(title="Single " + col + " Cell", ylabel="Matching Features Count", xlabel="Cell Type Average")
        ax.yaxis.set_tick_params(labelbottom=True)

    fig.tight_layout()
    fig.suptitle("Standard Deviation Classification", size=16)
    fig.subplots_adjust(top=0.88)
    plt.savefig("Figure4.png")
    return

figure_4_plots()