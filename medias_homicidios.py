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



def estimativas_variabilidade(dados_brutos, media):
    """
   Estimativas de Variabilidade
   Indica o quão espalhados/dispersos os dados estão em relação ao centro (média, mediana, moda)
      Desvios
      Diferença entre os valores observados e uma estimativa de localização (média, mediana, moda)
      - Desvio: tx_homicidio - media
      - Desvio Absoluto: |tx_homicidio - media|
      - Desvio Absoluto Médio: soma dos desvios / num desvios
      - Variância: soma(desvio^2) / num desvios - 1
      - Desvio Padrão: Raiz quadrada da variância
      Estatísticas de Ordem
      Estatísticas baseadas em dados ordenados (order)
      - Amplitude: valor máximo - valor mínimo
      - Percentil: Divide os valores em porcentagens           [10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%]
      - Quantil: Mesmo que percentil, mas com casas decimais   [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
      - Quartil: Divide os valores em quatro partes iguais     [Q1 = 25%, Q2 = 50%, Q3 = 75%]
      - Amplitude Interquartil: Q3 - Q1
      - Mediana: Divide os valores em duas partes iguais       [med = Q2]
         Percentis
   """
    print(estimativas_variabilidade.__doc__)
    # Ordenar os dados
    dados_brutos = dados_brutos.sort_values()
    # desvios 
    desvios = dados_brutos - media
    # desvios Absolutos 
    desvios_absolutos = np.abs(desvios)
    # desvios absolutos médios 
    desvio_absoluto_medio = np.mean(desvios_absolutos)
    # Variância (ddof = dlta degreee of freedom)
    variancia = np.var(dados_brutos, ddof=1)
    # desvio padrão 
    desvio_padrao = np.std(dados_brutos, ddof=1)
    # DataFrame 
    df_desvios_individuais = pd.DataFrame({
        'Dados Brutos': dados_brutos,
        'Desvio (taxa homicidos - media)': desvios,
        'Desvio Absoluto |tx_homicidio - media|': desvios_absolutos
        })
    df_media_desvios = pd.DataFrame({
        'Métrica Estatística' : [
            'Média',
            'Desvio Padrão',
            'variância',
            'Desvio Absoluto Médio (DAM)'
        ],
        'Valor Calculado': [
            media,
            desvio_padrao,
            variancia,
            desvio_absoluto_medio
        ]
    })
    # imprimir dados
    print(df_desvios_individuais.round(2))
    print("\n")
    print(df_media_desvios.round(2))
    print("\n")
    # quantil (decimais)
    decimais = [0.05, 0.25, 0.5, 0.75, 0.95]
    df_quartis = pd.DataFrame(dados_brutos.quantile(decimais))
    print(df_quartis.transpose())
    # percentil
    df_percentis = pd.DataFrame(dados_brutos.quantile(decimais))
    # ESTE CODIGO:
    # novo_indicis = []
    # for p in decimais
    #     novos_indicis.append(f"{p*100}%")
    # df_percentis.index = novos_indicis
    # RESUMISE EM:   "df_percentis.index = [f"{p*100}%" for p in decimais]"
    df_percentis.index = [f"{p*100}%" for p in decimais]
    print("\n")
    
    # Quartis
    quartis = [0.25, 0.5, 0.75]
    df_quartis = pd.DataFrame(dados_brutos.quantile(quartis))
    df_quartis.index = ['Q', 'Q2', 'Q3']
    print(df_quartis.transpose())
    # Amplitude
    amplitude = dados_brutos.max() - dados_brutos.min()
    amplitude_alt = dados_brutos.iloc[-1] - dados_brutos.iloc[0]
    # amplitud interquatil = Q3 - Q1
    amplitude_interquartil = df_quartis.max() - df_quartis.min()
    amplitude_interquartil_alt = dados_brutos.quantile(0.75) - dados_brutos.quantile(0.25)
    # mmediana
    mediana = dados_brutos.median()
    # DataFrame 
    df_amplitude = pd.DataFrame({
        'Amplitude (max - min)': amplitude,
        'Amplitude interquantil (Q3 - Q1)': amplitude_interquartil,
        'Mediana (Q2)': mediana
    })
    # Imprimir dados
    print(df_amplitude.round(2))
    
estimativas_variabilidade(df_dados_brutos['Taxa Homicídio'], np.mean(df_dados_brutos['Taxa Homicídio']))