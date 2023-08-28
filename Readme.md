# Explanation of Subdirectories

### Data
Raw data in the form of .csvs, .tsvs, or .xlsx
Primary = Cleaned from the Website
GSE118... = Figure 1 Cell line PCA 

### Processed Data
Functions that load the raw data into dataframes ready for use in comparison functions

### Comparisons
Functions that create gene standard deviation matrices as well as comparing various matrices for the purpose of classification

### Figures
Functions that produce the figures used in the manuscript

### Results
Directory used to store figures and results


# Reproducibility

All figures have a dedicated python script in the figures subdirectory to reproduce that figure. Run the appropriately named file to reproduce that figure.

The results.txt file is the results of the final classification data for figure 4. It is produced in the figure_4_plots.py file along with figure 4.

The stats_results.txt file is the results of chi-squared tests on the individual classifications as well as a binomial test on the classification process. It is dependent on the results.txt file that is generated in the figure_4_plots.py being in the 'results' subdirectory. The file is then generated by running the statistic_analysis_of_results.py file.

List of necessary libraries:
* numpy
* pandas
* regex
* seaborn
* matplotlib.pyplot
* matplotlib.colors
* json
* scipy.stats
