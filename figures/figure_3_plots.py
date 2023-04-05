from comparisons.create_brain_matrices import create_brain_matrices
from comparisons.compare_datasets import compare_dataset
from processed_data.load_brain_data import load_brain_data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors



def figure_3_plots():
    infile = "../data/GSE181153_ADAB_geneCounts.tsv"

    data_transpose, new_merge, grouped, mean_df, standard_df, test_df = load_brain_data(infile)
    matrices, sorted_indeces = create_brain_matrices(data_transpose, new_merge, grouped, mean_df, standard_df)
    final, figure_vals = compare_dataset(test_df, standard_df, mean_df, matrices, sorted_indeces)

    figure_df = pd.DataFrame(figure_vals)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 7), sharex=False, sharey=True)
    axes = axes.ravel()  # array to 1D
    cols = figure_vals.keys()
    for col, ax in zip(cols, axes):
        data = figure_df[col]  # select the data
        max_val = max(figure_vals[col][1])
        colors = [mcolors.TABLEAU_COLORS["tab:red"] if y == max_val else mcolors.CSS4_COLORS["lightsteelblue"] for y in figure_vals[col][1]]
        x_vals = figure_vals[col][0]
        for v in range(len(x_vals)):
            if x_vals[v] == "HMC3" or x_vals[v] == "iMGL" or x_vals[v] == "iPSC" or x_vals[v] == "iHPC":
                x_vals[v] = "(MG) " + x_vals[v]
            elif x_vals[v] == "U87a":
                x_vals[v] = "(Ast) " + x_vals[v]
            elif x_vals[v] == "PBMC" or x_vals[v] == "THP1":
                x_vals[v] = "(Mac) " + x_vals[v]
        sns.barplot(data=data, x=x_vals, y=figure_vals[col][1], ax=ax, palette=colors)
        ax.set(title="Single " + col + " Cell", ylabel="Matching Features Count", xlabel="Cell Type Average")
        ax.yaxis.set_tick_params(labelbottom=True)

    fig.tight_layout()
    fig.suptitle("Standard Deviation Classification", size=16)
    fig.subplots_adjust(top=0.88)
    plt.savefig("Figure3.png")
    return

figure_3_plots()