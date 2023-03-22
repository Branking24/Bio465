import pandas as pd
import numpy as np
import boxsdk as box

def load_cancer_data():
    config = box.JWTAuth.from_settings_file("../config/config.json")
    client = box.Client(config)
    omics_id = '1169438801565'
    model_id = '1169436718115'
    data_df = pd.read_csv(client.file(omics_id).content())
    data_df.columns.values[0] = "ModelID"

    model_df = pd.read_csv(client.file(model_id).content(), usecols=["ModelID", "DepmapModelType"])
    new_merge = pd.merge(data_df, model_df)

    new_merge = new_merge.replace(0, np.nan) # data normalization --> getting rid of 0s
    grouped = new_merge.groupby("DepmapModelType").mean()

    mean_df = grouped.mean()

    standard_df = grouped.std()

    return data_df, model_df, new_merge, grouped, mean_df, standard_df

load_cancer_data()