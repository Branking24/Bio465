from comparisons.create_brain_matrices import create_brain_matrices
from comparisons.compare_datasets import compare_dataset
from processed_data.load_brain_data import load_brain_data
import seaborn as sns
import matplotlib.pyplot as plt



def figure_3_plots():
    infile = "../data/GSE181153_ADAB_geneCounts.tsv"
    data_transpose, new_merge, grouped, mean_df, standard_df = load_brain_data(infile)
    matrices, sorted_indeces = create_brain_matrices()
    final, figure_vals = compare_dataset(data_transpose, standard_df, mean_df, matrices, sorted_indeces[:1000])
    print(figure_vals)
    for k in figure_vals.keys():
        #y_data = figure_vals[k][1].sort()
        sns.barplot(x=figure_vals[k][0], y=figure_vals[k][1]).set(title=k)
        plt.show()


    return

figure_3_plots()