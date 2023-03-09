import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_combined_data_frames(data_name, model_name, merge_column_name, column_id):
    data_df = pd.read_csv(data_name)
    data_df.columns.values[0] = column_id

    model_df = pd.read_csv(model_name, usecols=[column_id, merge_column_name])
    new_merge = pd.merge(data_df, model_df)

    new_merge = new_merge.replace(0, np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby(merge_column_name).mean()

    mean_df = grouped.mean()

    standard_df = grouped.std()

    return data_df, model_df, new_merge, grouped, mean_df, standard_df


def plot_figures(*argv):
    omics_df, model_df, new_merge, grouped, mean_df, standard = create_combined_data_frames(
        argv[0], argv[1], "DepmapModelType", "ModelID")
    to_plot = omics_df.iloc[:, 4]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True)
    plt.show()
    to_plot = omics_df.iloc[:, 3]
    to_plot_2 = to_plot[to_plot != 0]
    plot = sns.histplot(data=to_plot_2, kde=True)
    plt.show()
