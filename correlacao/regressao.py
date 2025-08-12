import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# 2. 
ESPOSICAO_ALGODAO = '../data/LungDisease.csv'
dataframe = pd.read_csv(ESPOSICAO_ALGODAO)
print("-" * 250)
print(dataframe.head())

# Gráfico DISPERSÃO
# dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
# plt.show()  

# 3. Configuração e treinamento do modelo 
# Define a variável preditora (independente), que é 
# a Exposure e a variável de resultado que é o PERF
predictors = ['Exposure']
outcome = 'PEFR'
# Iniciar o Modelo 
model = LinearRegression()
# Etapa de etreinamento
model.fit(dataframe[predictors], dataframe[outcome])

# 4. Exibção dos coeficiente
# intercepto
print("-" * 250)
print(f'Intercepto: {model.intercept_:.3f}')
# Coeficiente Angular
print("-" * 250)
print(f'Coeficiente Angular: {model.coef_[0]}')

# 5. Geração dos Gáficos 
fig, (reg) = plt.subplots(1, 1, figsize=(4, 4))
# Gráfico regreção
reg = sns.regplot(x= 'Exposure', y = 'PEFR', data = dataframe, ax = reg)
plt.tight_layout()
plt.show()