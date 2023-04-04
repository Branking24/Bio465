import pandas as pd
import regex as re
import numpy as np


def load_primary_tissue_data(*argv):


    data_df = pd.read_csv(argv[0])

    pattern = r'.[0-9]'
    renamed_data = data_df.rename(columns=lambda x: re.sub('Human', '', x))
    renamed_data = renamed_data.rename(columns=lambda x: re.sub(pattern, '', x))
    renamed_data = renamed_data.rename(columns=lambda x: "astrocyte" if "mature astrocytes" in x else x.lstrip())
    renamed_data = renamed_data.rename(columns=lambda x: "astrocyte" if "astrocyte" and x != "astrocyte" in x else x.lstrip())

    data_o = renamed_data.transpose()
    data_o.columns = data_o.iloc[0]
    data_o = data_o.drop(['Gene'])

    join_df = pd.read_csv(argv[1], sep='\t')
    join_df = join_df.drop('ensembl', axis=1)

    renamed_data = join_df.rename(columns=lambda x: re.sub('ADAB_RNA_', '', x))
    renamed_data = renamed_data.rename(columns=lambda x: re.sub('_.*', '', x))

    join_transpose = renamed_data.transpose()
    join_transpose.columns = join_transpose.iloc[0]
    join_transpose = join_transpose.drop(['hgnc'])

    frames = [data_o, join_transpose]

    common_cols = list(set.intersection(*(set(df.columns) for df in frames)))
    common_cols = sorted(common_cols)
    data_transpose = data_o[common_cols]

    data_transpose = data_transpose.loc[:,~data_transpose.columns.duplicated()].copy()
    test_df = join_transpose[common_cols]
    test_df = test_df.loc[:, ~test_df.columns.duplicated()].copy()

    data_transpose.drop('Neurons', inplace=True)
    new_merge = data_transpose.replace(0, np.nan)  # data normalization --> getting rid of 0s

    grouped = new_merge.groupby(level=0).mean()

    mean_df = grouped.mean()

    standard_df = new_merge.std()

    return data_transpose, new_merge, grouped, mean_df, standard_df, test_df


