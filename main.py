import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# model.csv : cols 1 and 9
def main():
    omics_df = pd.read_csv("OmicsExpressionProteinCodingGenesTPMLogp1.csv")
    omics_df.columns.values[0] = "ModelID"

    model_df = pd.read_csv("Model.csv", usecols=['ModelID', 'DepmapModelType'])
    new_merge = pd.merge(omics_df, model_df)

    new_merge = new_merge.replace(0, pd.np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby("DepmapModelType").mean()

    #Get mean based on gene
    mean_df = grouped.mean()


    #Create Kernel Density Plots
    #plot = sns.histplot(data=new_merge.iloc[:, 1], kde=True)
    #plt.show()

    standard = grouped.std()


    #Per Cell Type, Find Relative Relationship


    #Compare Training Cells to Gene-Gene Matrices


    #Repeat for cell lines


    return

if __name__ == '__main__':
    main()


