import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr


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

def density_plot(to_plot, index):
    plot = sns.histplot(data=to_plot.iloc[:, index], kde=True)
    plot.show()

def compare_dataset(csv_name, csv_model_name, column_id, merge_column_name, standard_deviation, means, relationship_matrix):
    training_df = pd.read_csv(csv_name)
    training_df.columns.values[0] = column_id
    training_model_df = pd.read_csv(csv_model_name, usecols=[column_id, merge_column_name])

    merged = pd.merge(training_df, training_model_df)
    final = []
    cur_relation = []
    relationship = {}
    for i in range(len(merged.axes[0])):
        cur_relation = []
        relationship[merged.axes[0][i]] = []
        for j in range(1, len(merged.iloc[i].axes[0]) - 1):
            cur_val = merged.iloc[i].iloc[j]
            if cur_val == 0:
                relationship[merged.axes[0][i]].append(0)
            elif cur_val > (means.iloc[j - 1] + standard_deviation.iloc[j - 1]):
                relationship[merged.axes[0][i]].append(1)
            elif cur_val < (means.iloc[j - 1] - standard_deviation.iloc[j - 1]):
                relationship[merged.axes[0][i]].append(-1)
            else:
                relationship[merged.axes[0][i]].append(0)

        for l in range(len(relationship[merged.axes[0][i]])):
            for j in range(l, len(relationship[merged.axes[0][i]])):
                if relationship[merged.axes[0][i]][l] == 1 and relationship[merged.axes[0][i]][j] == -1:
                    cur_relation.append(-1)
                elif relationship[merged.axes[0][i]][l] == -1 and relationship[merged.axes[0][i]][l] == 1:
                    cur_relation.append(1)
                else:
                    cur_relation.append(0)

        max = 0
        max_s = ""
        for k in relationship_matrix.keys():
            cur, p = spearmanr(relationship_matrix[k], cur_relation)
            if abs(cur) > max:
                max = abs(cur)
                max_s = k
        final.append(max_s)
    return

# model.csv : cols 1 and 9
def main():
    
    '''omics_df = pd.read_csv("OmicsExpressionProteinCodingGenesTPMLogp1.csv")
    omics_df.columns.values[0] = "ModelID"

    model_df = pd.read_csv("Model.csv", usecols=['ModelID', 'DepmapModelType'])
    new_merge = pd.merge(omics_df, model_df)

    new_merge = new_merge.replace(0, pd.np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby("DepmapModelType").mean()

    #Get mean based on gene
    mean_df = grouped.mean()


    standard = grouped.std()'''

    omics_df, model_df, new_merge, grouped, mean_df, standard = create_combined_data_frames("OmicsExpressionProteinCodingGenesTPMLogp1.csv", "Model.csv", "DepmapModelType", "ModelID")


    #Per Cell Type, Find Relative Relationship
    relations = {}
    final = {}
    for i_type in range(len(grouped.axes[0])):
        type = grouped.axes[0][i_type]
        relations[type] = []
        final[type] = []
        for gene in range(len(mean_df.axes[0])):
            if grouped.iloc[i_type, gene] > mean_df.iloc[gene] + standard.iloc[gene]:
                relations[type].append(1)
            elif grouped.iloc[i_type, gene] < mean_df.iloc[gene] - standard.iloc[gene]:
                relations[type].append(-1)
            else:
                relations[type].append(0)

        for i in range(len(relations[type])):
            for j in range(i, len(relations[type])):
                if relations[type][i] == 1 and relations[type][j] == -1:
                    final[type].append(-1)
                elif relations[type][i] == -1 and relations[type][j] == 1:
                    final[type].append(1)
                else:
                    final[type].append(0)

    #Compare Training Cells to Gene-Gene Matrices
    predict = compare_dataset("Training.csv", "Model_training.csv", "ModelID", "DepmapModelType", standard, mean_df, final)
    print(predict)
    #Repeat for cell lines


    return

if __name__ == '__main__':
    main()


