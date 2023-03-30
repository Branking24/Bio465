from comparisons.create_brain_matrices import create_brain_matrices
from comparisons.compare_datasets import compare_dataset
from processed_data.load_brain_data import load_brain_data
from processed_data.load_primary_tissue_data import load_primary_tissue_data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors



def figure_3_plots():
    infile = "../data/GSE181153_ADAB_geneCounts.tsv"
    infile2 = "../data/primary_brain_data.csv"
    data_transpose2, new_merge2, grouped2, mean_df2, standard_df2 = load_primary_tissue_data(infile2)
    data_transpose, new_merge, grouped, mean_df, standard_df, test_df = load_brain_data(infile)
    matrices, sorted_indeces = create_brain_matrices()
    final, figure_vals = compare_dataset(test_df, standard_df, mean_df, matrices, sorted_indeces[:100])
    print(figure_vals)
    figure_df = pd.DataFrame(figure_vals)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 7), sharex=False, sharey=False)
    axes = axes.ravel()  # array to 1D
    cols = figure_vals.keys()
    for col, ax in zip(cols, axes):
        data = figure_df[col]  # select the data
        max_val = max(figure_vals[col][1])
        colors = [mcolors.TABLEAU_COLORS["tab:red"] if y == max_val else mcolors.CSS4_COLORS["lightsteelblue"] for y in figure_vals[col][1]]
        sns.barplot(data=data, x=figure_vals[col][0], y=figure_vals[col][1], ax=ax, palette=colors)
        ax.set(title="Single " + col + " Cell", ylabel="Matching Features Count", xlabel="Cell Type Average")

    #fig.delaxes(axes[15])  # delete the empty subplot
    fig.tight_layout()
    fig.suptitle("Standard Deviation Classification", size=16)
    fig.subplots_adjust(top=0.88)
    plt.savefig("Figure3.pdf")
    return

figure_3_plots()