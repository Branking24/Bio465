import pandas as pd
import regex as re
import numpy as np


def load_primary_tissue_data(*argv):

    data_df = pd.read_csv(argv[0])

    pattern = r'.[0-9]'
    renamed_data = data_df.rename(columns=lambda x: re.sub('Human', '', x))
    renamed_data = renamed_data.rename(columns=lambda x: re.sub(pattern, '', x))

    data_transpose = renamed_data.transpose()
    data_transpose.columns = data_transpose.iloc[0]
    data_transpose = data_transpose.drop(['Gene'])

    new_merge = data_transpose.replace(0, np.nan)  # data normalization --> getting rid of 0s

    grouped = new_merge.groupby(level=0).mean()

    mean_df = grouped.mean()

    standard_df = new_merge.std()

    return data_transpose, new_merge, grouped, mean_df, standard_df


load_primary_data("/Users/myannamoody/Bio465/data/primary_brain_data.csv")
