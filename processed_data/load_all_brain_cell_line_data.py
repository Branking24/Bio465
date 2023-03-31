import pandas as pd
import regex as re
import numpy as np

def load_all_brain_cell_line_data(*argv):
    # data = "../data/GSE181153_ADAB_geneCounts.tsv"
    # out_filepath = "../data/processed_brain_data.csv"

    data_df = pd.read_csv(argv[0], sep='\t')

    data_df = data_df.drop('ensembl', axis=1)

    renamed_data = data_df.rename(columns=lambda x: re.sub('ADAB_RNA_','',x))
    renamed_data = renamed_data.rename(columns=lambda x: re.sub('_.*','',x))

    data_transpose = renamed_data.transpose()
    data_transpose.columns = data_transpose.iloc[0]
    data_transpose = data_transpose.drop(['hgnc'])

    new_merge = data_transpose.replace(0, np.nan) # data normalization --> getting rid of 0s

    return data_transpose, new_merge

