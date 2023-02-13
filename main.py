import pandas as pd

# model.csv : cols 1 and 9
def main():
    omics_df = pd.read_csv("OmicsExpressionProteinCodingGenesTPMLogp1.csv")
    omics_df.columns.values[0] = "ModelID"

    model_df = pd.read_csv("Model.csv", usecols=['ModelID', 'DepmapModelType'])
    new_merge = pd.merge(omics_df, model_df)

    new_merge = new_merge.replace(0, pd.np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby("DepmapModelType").mean()
    return

if __name__ == '__main__':
    main()


