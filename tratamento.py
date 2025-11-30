import pandas as pd

df = pd.read_csv("run_ww_2020_m.csv")

# Removendo outliers e deixando apenas meio maratonistas
df_rem_out = df[(df["duration"] <= 150) & (df["duration"] >= 50) & (df["distance"] >= 18) & (df["distance"] <= 22)]

df_rem_out = df_rem_out.drop(["major", "athlete", "country"], axis=1).dropna()

df_rem_out = df_rem_out.rename(columns={"Unnamed: 0": "id"})

# print(df_rem_out.count()) # Verificando coerência entre quantidade e tipos

df_sep_M = df_rem_out[df_rem_out['gender'] == 'M']
df_sep_M = df_sep_M.reset_index(drop=True)
df_sep_M["id"] = df_sep_M.index

df_sep_F = df_rem_out[df_rem_out['gender'] == 'F']
df_sep_F = df_sep_F.reset_index(drop=True)
df_sep_F["id"] = df_sep_F.index

df_sep_F.to_csv("21Km_Mulheres.csv", index = False)
df_sep_M.to_csv("21Km_Homens.csv", index = False)

# print('Mulheres: ' + str(df_sep_F['gender'].count()), 'Homens: ' + str(df_sep_M['gender'].count()))
print(df_sep_M.head())


