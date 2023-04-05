import pandas as pd
import regex as re
import numpy as np

def load_brain_data(*argv):

    data_df = pd.read_csv(argv[0], sep='\t')

    data_df = data_df.drop('ensembl', axis=1)

    renamed_data = data_df.rename(columns=lambda x: re.sub('ADAB_RNA_','',x))
    renamed_data = renamed_data.rename(columns=lambda x: re.sub('_.*','',x))

    data_transpose = renamed_data.transpose()
    data_transpose.columns = data_transpose.iloc[0]
    data_transpose = data_transpose.drop(['hgnc'])

    data_transpose = data_transpose.reset_index()


    new_merge = data_transpose.replace(0, np.nan) # data normalization --> getting rid of 0s

    #2,8,12,16
    row_iMGL = new_merge.iloc[2]
    row_HMC3 = new_merge.iloc[8]
    row_U87a = new_merge.iloc[12]
    row_PBMC = new_merge.iloc[17]
    test_df = pd.concat([row_iMGL, row_HMC3, row_U87a, row_PBMC], axis=1).T
    test_df.set_index("index", inplace=True)
    new_merge.drop(new_merge.index[2], inplace=True)
    new_merge.drop(new_merge.index[7], inplace=True)
    new_merge.drop(new_merge.index[10], inplace=True)
    new_merge.drop(new_merge.index[14], inplace=True)
    new_merge.set_index("index", inplace=True)
    data_transpose.set_index("index", inplace=True)

    grouped = new_merge.groupby(level=0).mean()

    mean_df = grouped.mean()

    standard_df = new_merge.std()

    return data_transpose, new_merge, grouped, mean_df, standard_df, test_df

