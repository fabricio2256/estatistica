import pandas as pd
import numpy as np
from faker import Faker 

# Geração dos dados 
faker = Faker('pt_BR')

# Gerar notas 
media_notas = 70
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc=media_notas, scale=desvio_padrao_notas, size=num_alunos)
notas = np.clip(notas, 0, 100).astype(int)
# simples 
notas_simples = np.random.randint(0, 101, size=100)

# Nome alunos 
nome_alunos = [faker.name( )for _ in range(num_alunos)]
df_alunos = pd.DataFrame({
    'Nome':nome_alunos,
    'Nota': notas 
})
print("--- DfataFrame Alunos e Notas---")
print(df_alunos.head())

# --Cáuculos de Quartís
q1 = df_alunos['Nota'].quantile(0.25)
q2 = df_alunos['Nota'].quantile(0.50)
q3 = df_alunos['Nota'].quantile(0.75)
df_quartis = pd.DataFrame({
    'Quartil': ['Primeiro (Q1)', 'Segundo (Q2 = Mediana)', 'Terceiro (Q3)'],
    'Valor': [q1, q2, q3]
})
print("---Quartis das Notas---")
print(df_quartis)
print("\n")

# --- Cáuculos das Decis
decis_percentis = [i /10.0 for i in range(1, 11)]
decis_valores = [df_alunos['Nota'].quantile(p) for p in decis_percentis]
decis_nomes = [f"{i}° Decil" for i in range(1, 11)]
print(decis_nomes)
df_decis= pd.DataFrame({
    'Decil': decis_nomes,
    'Percentil': [f"{int(p*100)}%" for p in decis_percentis],
    'Valor': decis_valores
})
print("---  Decis das nota s ---")
print(df_decis)
print("\n")

amplitude_interquantil = q3 - q1

df_aiq =  pd.DataFrame({
    'Métrica': ['Amplitude Interquantil (AIQ)'],
    'Valor': [amplitude_interquantil]
})
print("---Amplitude Interquantil (ATQ)---")
print(df_aiq)
print("\n")