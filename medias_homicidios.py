# venv\Scripts\activate
# .\venv\Scripts\activate
# venv\Scripts\activate.sp1
import pandas as pd 
import numpy as np
# pip install scipy
from scipy.stats import trim_mean

# Medias do arquivo
def get_media (df_dados_brutos):
    # medias simples :
    media_populacao  = df_dados_brutos['População'].mean()
    media_homicidios = df_dados_brutos['Taxa Homicídio'].mean() 
    # medias aparadas
    proporcao_corte = 0.1 #corte de 10% de cada ponta 
    media_aparada_populacao = trim_mean(df_dados_brutos['População'], proportiontocut=proporcao_corte)
    media_aparada_homicidios = trim_mean(df_dados_brutos['Taxa Homicídio'], proportiontocut=proporcao_corte)
    # medianas 
    mediana_populacao = df_dados_brutos['População'].median()
    mediana_homicidios = df_dados_brutos['Taxa Homicídio'].median()
    # media ponderada = soma(valor * peso) / soma(peso)
    # onde valor é a taxa_homicidios e o peso é população 
    # calcular a média ponderada de homicídios onde o peso de cada cidade é sua população 
    media_ponderada = np.average(df_dados_brutos['Taxa Homicídio'], weights=df_dados_brutos['População'])
    
    df_medias = pd.DataFrame({
        'População' : [media_populacao, media_aparada_populacao, mediana_populacao, np.nan],
        'Taxa Homicídio' : [media_homicidios, media_aparada_homicidios, mediana_homicidios, media_ponderada]
    }, index = ['Média', 'Média Aparada', 'Mediana', 'Média Ponderada'])
    return df_medias

df_dados_brutos = pd.read_csv('taxa_homicidios.csv')
print(df_dados_brutos)
df_medias = get_media(df_dados_brutos)
print({df_medias.to_string(float_format="%2.f")})
