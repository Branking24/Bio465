# Explanation of Subdirectories

### Data
Raw data in the form of .csvs, .tsvs, or .xlsx

### Processed Data
Functions that load the raw data into dataframes ready for use in comparison functions

### Comparisons
Functions that create gene standard deviation matrices as well as comparing various matrices for the purpose of classification

### Figures
Functions that produce the figures used in the manuscript

### Results
Directory used to store figures


# Reproducibility

All figures have a dedicated python script in the figures subdirectory to reproduce that figure. Run the appropriately named file to reproduce that figure.

List of necessary libraries:
* numpy
* pandas
* regex
* seaborn
* matplotlib.pyplot
* matplotlib.colors