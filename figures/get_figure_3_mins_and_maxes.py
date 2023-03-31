import pandas as pd
import regex as re
import numpy as np
from processed_data.load_all_brain_cell_line_data import load_all_brain_cell_line_data
from comparisons.create_brain_matrices import create_brain_matrices
from comparisons.compare_datasets import compare_dataset
def load_training_data(test_index, o_new_merge):

    new_merge = o_new_merge.copy().reset_index()

    test_df = new_merge.iloc[test_index].to_frame().T
    new_merge.drop(new_merge.index[test_index], inplace=True)
    test_df.set_index("index", inplace=True)
    new_merge.set_index("index", inplace=True)

    grouped = new_merge.groupby(level=0).mean()

    mean_df = grouped.mean()

    standard_df = new_merge.std()

    return new_merge, grouped, mean_df, standard_df, test_df

def get_mins_and_maxes():
    infile = "../data/GSE181153_ADAB_geneCounts.tsv"
    outfile = "../data/figure_3_mins_and_maxes.txt"
    data_transpose, orig_new_merge = load_all_brain_cell_line_data(infile)
    vals = {}
    for i in range(len(data_transpose.axes[0])):
        new_merge, grouped, mean_df, standard_df, test_df = load_training_data(i, orig_new_merge)
        matrices, sorted_indeces = create_brain_matrices(data_transpose, new_merge, grouped, mean_df, standard_df)
        final, figure_vals = compare_dataset(test_df, standard_df, mean_df, matrices, sorted_indeces[:100])
        for v in figure_vals.keys():
            if v not in vals:
                vals[v] = [figure_vals[v][1],figure_vals[v][1]]
            else:
                for n in range(len(figure_vals[v][1])):
                    if figure_vals[v][1][n] < vals[v][0][n]:
                       vals[v][0][n] = figure_vals[v][1][n]
                    if figure_vals[v][1][n] > vals[v][1][n]:
                        vals[v][1][n] = figure_vals[v][1][n]

    print(vals)
    out = open(outfile,"w")

    for k in vals.keys():
        out.write(k + '\n')
        out.writelines(vals[k][0])
        out.writelines(vals[k][1])
    out.close()
    return

get_mins_and_maxes()