import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data/sp500_data.csv.gz'
df = pd.read_csv(data)

# Remover coluna específica 
df = df.drop(columns=['ADS'])

# Renomear coluna específica 
df = df.rename(columns={'Unnamed: 0': 'Data'})

# Transformar o campo data para DataTime e settar ele como indice 
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')
print(df.head())

# Encontrar a maior e menor data
data_inicio = df.index.min()
data_fim = df.index.max()
print("-" * 50)
print(f"Quantidade de variações coletadas:{len(df)}")
print(f"Período de coleta: {data_inicio.strftime('%d/%m/%Y')} á {data_fim.strftime('%d/%m/%Y')}")

# Guardar o Ativio sendo usado
ativo = 'IBM'

# Encontrar o valor máximo e mínimo do ativo 
maior_valor = df[ativo].max()
data_maior = df[ativo].idxmax()
menor_valor = df[ativo].min()
data_menor = df[ativo].idxmin()
print("-" * 50)
print(f"Ativo: {ativo}")
print(f'Valor máximo do Ativo: {maior_valor:.4f}')
print(f'Data do menor Valor: {data_maior.strftime('%d/%m/%Y')}')
print(f'Valor máximo do Ativo: {menor_valor:.4f}')
print(f'Data do menor Valor: {data_menor.strftime('%d/%m/%Y')}')

# MEDIAS DE TENDÊNCIA CENTRAL
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df[ativo].mode()
print("-" * 50)
print(f"Medidas de tendência central para {ativo}:")
print(f"Média: {media:.4f}")
print(f"Mediana: {mediana:.4f}")
if (len(moda) > 0):
    print(f"Modas: {moda}")
else : 
    print(f"O ativo {ativo} é amodal")