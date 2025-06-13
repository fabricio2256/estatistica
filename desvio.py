import pandas as pd 
import numpy as np
from faker import Faker

# instância do Fakerr para gerar nomes 
faker = Faker('pt_BR')

# Condições dos dados [População]
media_notas = 70 
desvio_padrao_notas = 10
num_alunos = 100
notas = np.random.normal(loc = media_notas, scale = desvio_padrao_notas, size = num_alunos)
print(f"Notas random: {notas}")
# Limite as notas entre 0 e 100
# O que for menor que 0 vira 0 e o que for maior que 100 vira 100
notas = np.clip(notas, 0, 100)

# ---CALCULOS DAS MÉDIAS ---
# 1. Média 
print(f"----------------  MÉDIA  ----------------")
media = np.mean(notas)
print(f"{media}")

# 2. Mediana 
print(f"----------------  MEDIANA  ----------------")
mediana = np.median(notas)
print(f"{mediana}")

# 3. Desvios (Simples)
print("----------------  DESVIOS (SIMPLES)  ----------------")
desvios = notas - media
print(f"{desvios}")

# 4.Desvio Absoluto
# ex: 80(nota) - 70(media) = |10|(desvio)
print("----------------  Desvio Absoluto  ----------------")
desvio_absoluto = np.abs(notas - media)
print(f"{desvio_absoluto}")

# 5. Variância Individual
# ex: 80(nota) - 70(media) = 10 * 10 = 100(Variância)
print("----------------  Variância Individual  ----------------")
variancias_individuais = (notas - media)**2
variancia = np.var(notas, ddof=1)#para variância amostral (n-1)
print(f"{variancia}")

# 6.Desvio Padrão
print("----------------  Desvio Padrão  ----------------")
desvio_padrao = np.std(notas)
print(f"{desvio_padrao}")

# 7. Desvio Absoluto (Mediana)
print("----------------  Desvio Absoluto (Mediana)  ----------------")
desvio_abs_em_relacao_mediana_individuais = np.abs(notas - mediana)
mad = np.median(desvio_abs_em_relacao_mediana_individuais)
print(f"desvio_abs_em_relacao_mediana_individuais")

# 8. Desvio Absoluto Médio
print("----------------  Desvio Absoluto Médio  ----------------")
dam = np.mean(desvio_absoluto)
print(f"Desvio Absoluto Médio")

# CRIAÇÃO DATAFRAME
print("---DataFrame 1; dados Brutos, Desvios e Variância individuais")
df_detalhes = pd.DataFrame({
    'Dados Brutos' : notas,
    'Dwesvios (x - media)' : desvios,
    'Variância Individual (x - (média)^2': variancias_individuais,
    'Desvio Absolutop (x - média)': desvio_absoluto,
    'Desvio Absolutop (x - mediana)': desvio_abs_em_relacao_mediana_individuais    
})
# imprimeir apenas 10 das 100 notas, e arredondar para 2 casas decimais
print(df_detalhes.head(10).round(2))

resultados_estatisticos_unicos = {
    'Métrica Estatística': [
        'Média',
        'Mediana',
        'Desvio Padrão',
        'VariâNCIA',
        'Desvio Absoluto Médio (DAM)',
        'Dsvio Absoluto Mediano (MAD)'
    ],
    'Valor Calculado': [
    media,
    mediana,
    desvio_padrao,
    variancia,
    dam,
    mad    
    ]
    
} 
df_resultados_unicos = pd.DataFrame(resultados_estatisticos_unicos)
print(df_resultados_unicos.round(3))