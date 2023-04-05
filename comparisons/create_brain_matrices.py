import numpy as np

def create_brain_matrices(data_df, new_merge, grouped, mean_df, standard):
    relations = {}
    final = {}
    gene_names = []
    for gene in range(500):
        gene_names.append(mean_df.axes[0][gene])

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

    importance = []
    for i in range(len(relations[type])):
        cur = 0
        for k in final.keys():
            cur += abs(relations[k][i])
        importance.append(cur)

    np_array = np.array(importance)
    sorted_index_pos = [index for index, num in sorted(enumerate(np_array), key=lambda x: x[-1])][::-1]
    return relations, sorted_index_pos