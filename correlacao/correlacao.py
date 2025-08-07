import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho para os data set
ATIVOS_CSV = '../data/sp500_data.csv.gz'
SETORES_CSV = '../data/sp500_sectors.csv'

print("-" * 250)

df_ativos = pd.read_csv(ATIVOS_CSV, index_col=0)
print(df_ativos.head())
print("-" * 250)
df_setores = pd.read_csv(SETORES_CSV)
print(df_setores.head())
print("-" * 250)

# Telecomunicações 
df_telecom = df_setores[df_setores['sector'] == 'telecommunications_services']['symbol']
print(df_telecom)
print("-" * 250)

# Ativos Telecomunicativos 
telecom_ativos = df_ativos.loc[df_ativos.index >= '2012-07-01', df_telecom]
print(telecom_ativos.head())
print("-" * 250)

# Correlação  
dados_correlacionados = telecom_ativos.corr()
print(dados_correlacionados.head())
print("-" * 250)

# ETFs
df_etf = df_ativos.loc[df_ativos.index > '2012-07-01', df_setores[df_setores['sector'] == 'etf']['symbol']]
print(df_etf.head())
print("-" * 250)

etfs_correlacionados = df_etf.corr()
print(etfs_correlacionados.head())
print("-" * 250)

# GRÁFICOS DE CALOR
fig, (telecomax, etfax) = plt.subplots(1, 2, figsize = (10, 5))

telecomax = sns.heatmap(telecom_ativos.corr(), vmin = -1, vmax = 1, cmap=sns.diverging_palette(20, 220, as_cmap = True), ax= telecomax)

etfax = sns.heatmap(df_etf.corr(), vmin = -1, vmax = 1, cmap = sns.diverging_palette(20, 220, as_cmap=True), ax=etfax)

plt.tight_layout()
plt.show()