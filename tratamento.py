import pandas as pd

df = pd.read_csv("run_ww_2020_m.csv")

# Removendo outliers e deixando apenas meio maratonistas
df_rem_out = df[(df["duration"] <= 150) & (df["duration"] >= 50) & (df["distance"] >= 18) & (df["distance"] <= 22)]

df_rem_out = df_rem_out.drop("major", axis=1)

# print(df_rem_out[df_rem_out.isna().any(axis=1)])

# print(df_rem_out.isna().any(axis=1).sum()) # Linhas que serão removidas (Nan)

df_rem_nan = df_rem_out.dropna() # Removendo valores Nan

print(df_rem_nan.head(5))
# print(df_rem_nan[df_rem_nan.isna().any(axis=1)])

# print(df_rem_nan.count()) # Verificando coerência entre quantidade e tipos

# print(df_rem_nan.dtypes)



