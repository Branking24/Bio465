
def compare_dataset(merged, standard_deviation, means, relationship_matrix, sorted_indeces):

    final = []
    relationship = {}
    figure_vals = {}
    for i in range(len(merged.axes[0])):
        relationship[merged.axes[0][i]] = []
        for j in range(len(means.axes[0])):
            cur_val = merged.iloc[i].iloc[j]
            if cur_val == 0:
                relationship[merged.axes[0][i]].append(0)
            elif cur_val > (means.iloc[j - 1] + standard_deviation.iloc[j - 1]):
                relationship[merged.axes[0][i]].append(1)
            elif cur_val < (means.iloc[j - 1] - standard_deviation.iloc[j - 1]):
                relationship[merged.axes[0][i]].append(-1)
            else:
                relationship[merged.axes[0][i]].append(0)

        max = 0
        max_s = ""
        cur_set = [[],[]]
        for k in relationship_matrix.keys():
            cur = 0
            for m in range(len(relationship_matrix[k])):
                if m in sorted_indeces and relationship[merged.axes[0][i]][m] == relationship_matrix[k][m]:
                    cur += 1
            cur_set[0].append(k)
            cur_set[1].append(abs(cur))
            if abs(cur) > max:
                max = abs(cur)
                max_s = k
        figure_vals[merged.axes[0][i]] = cur_set
        final.append((merged.axes[0][i], max_s))
    return final, figure_vals