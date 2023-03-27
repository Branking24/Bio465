def create_matrices(grouped, mean_df, standard):
    relations = {}
    final = {}
    for i_type in range(len(grouped.axes[0])):
        type = grouped.axes[0][i_type]
        relations[type] = []
        final[type] = []
        # for gene in range(len(mean_df.axes[0])):
        for gene in range(500):
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
    return final