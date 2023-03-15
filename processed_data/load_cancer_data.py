import pandas as pd
import numpy as np

def load_cancer_data(data_name, model_name, merge_column_name, column_id):
    data_df = pd.read_csv(data_name)
    data_df.columns.values[0] = column_id

    model_df = pd.read_csv(model_name, usecols=[column_id, merge_column_name])
    new_merge = pd.merge(data_df, model_df)

    new_merge = new_merge.replace(0, np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby(merge_column_name).mean()

    mean_df = grouped.mean()

    standard_df = grouped.std()

    return data_df, model_df, new_merge, grouped, mean_df, standard_df