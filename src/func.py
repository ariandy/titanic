import pandas as pd

def custom_info(df, mode='all'):
    data_features = df.columns
    data_type = []
    null = []
    null_pct = []
    unique = []
    uniqueSample = []

    for item in data_features :
        data_type.append(str(df[item].dtype))
        null.append(sum(df[item].isnull()))
        null_pct.append(round(df[item].isna().sum()/len(df)*100,2))
        unique.append(df[item].nunique())
        uniqueSample.append(df[item].sample(3).values)

    desc = pd.DataFrame({
        'dataFeatures' : data_features,
        'dataType' : data_type,
        'null' : null,
        'nullPct' : null_pct,
        'unique' : unique,
        'uniqueSample' : uniqueSample
    })

    if mode == 'missing_values_only':
        desc = desc[desc.null>0].reset_index(drop=True).drop(['unique', 'uniqueSample'], axis=1)
    return desc