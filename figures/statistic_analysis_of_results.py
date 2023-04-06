import json
from scipy.stats import chisquare
def statistic_analysis_of_results():
    with open('../results/results.txt') as f:
        data = f.read()
    figure_vals = json.loads(data)

    stats_p_vals = {}

    for k in figure_vals.keys():
        x, p = chisquare(figure_vals[k][1])
        stats_p_vals[k] = p

    correct = 0
    failure = 0

    for k in figure_vals.keys():
        max_i = 0
        max_val = 0
        for i in range(len(figure_vals[k][1])):
            if figure_vals[k][1][i] > max_val:
                max_val = figure_vals[k][1][i]
                max_i = i

        if k == 'iMGL':
            if figure_vals[k][0][max_i] == 'Microglia/Macrophage':
                correct += 1
            else:
                failure += 1

        if k == 'U87a':
            if figure_vals[k][0][max_i] == 'astrocyte':
                correct += 1
            else:
                failure += 1

        if k == 'THP1':
            if figure_vals[k][0][max_i] == 'Microglia/Macrophage':
                correct += 1
            else:
                failure += 1

        if k == 'PBMC':
            if figure_vals[k][0][max_i] == 'Microglia/Macrophage':
                correct += 1
            else:
                failure += 1

        success_probability = 0.25

        binom_val = (success_probability ** correct) * ((1 - success_probability) ** failure)

        with open('stats_results.txt', 'w') as file:
            for k in stats_p_vals.keys():
                file.write(k + " p value = " + str(stats_p_vals[k]) + '\n')
            file.write("\n\nbinomial p value = " + str(binom_val))
            file.close()
    return

statistic_analysis_of_results()