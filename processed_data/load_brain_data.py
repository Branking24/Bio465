import pandas as pd
import regex as re
import numpy as np

def load_brain_data(*argv):
    # data = "../data/GSE181153_ADAB_geneCounts.tsv"
    # out_filepath = "../data/processed_brain_data.csv"

    data_df = pd.read_csv(argv[0], sep='\t')

    data_df = data_df.drop('ensembl', axis=1)

    renamed_data = data_df.rename(columns=lambda x: re.sub('ADAB_RNA_','',x))
    renamed_data = renamed_data.rename(columns=lambda x: re.sub('_.*','',x))

    data_transpose = renamed_data.transpose()
    data_transpose.columns = data_transpose.iloc[0]
    data_transpose = data_transpose.drop(['hgnc'])

    # data_transpose.to_csv(out_filepath)

    # data_df.columns.values[0] = column_id

    # model_df = pd.read_csv(model_name, usecols=[column_id, merge_column_name])
    # new_merge = pd.merge(data_df, model_df)

    new_merge = data_transpose.replace(0, np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby(level=0).mean()

    mean_df = grouped.mean()

    standard_df = new_merge.std()

    return data_transpose, new_merge, grouped, mean_df, standard_df

