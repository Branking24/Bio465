from scipy.stats import spearmanr

def compare_dataset(merged, standard_deviation, means, relationship_matrix):

    final = []
    relationship = {}
    for i in range(5):
        cur_relation = []
        relationship[merged.axes[0][i]] = []
        for j in range(100):
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
        final.append((merged.axes[0][i], max_s))

    return final