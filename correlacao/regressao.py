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
print(f'Intercepto: {model.intercept_:.3f}')
print("-" * 250)
# Coeficiente Angular
print(f'Coeficiente Angular: {model.coef_[0]}')
print("-" * 250)
# 5. Geração dos Gáficos 
fig, (reg, ax, res) = plt.subplots(1, 3, figsize=(14, 4))
# Gráfico regreção
reg = sns.regplot(x= 'Exposure', y = 'PEFR', data = dataframe, ax = reg)

# Parcial
# Definir os limites dos eixos X e Y
ax.set_xlim(0, 23)
ax.set_ylim(295, 450)
# Definir os rótulos 
ax.set_xlabel('Exposure')
ax.set_ylabel('PERF')
# Plotar a linha 
ax.plot(dataframe['Exposure'], model.predict(dataframe[predictors]), '-')
# Adicionar o texto b0
ax.text(0.4, model.intercept_, r'$b_0$', size = 'larger')
# Criar dataframe dos dados parciais treinar 
x = pd.DataFrame({'Exposure': [7.5, 17.5]})
y = model.predict(x)
ax.plot((7.5, 7.5, 17.5), (y[0], y[1], y[1]), '--')
# exibir DELtaY e DELtaX no Gráfico
ax.text(5, np.mean(y), r'$\Delta Y$', size = 'larger')
ax.text(12, y[1] - 10, r'$\Delta X$', size = 'larger')
# Adicionar anotações para  o coeficiente angular
ax.text(12, 390, r'$b_1 = \frac{\Delta Y}{\Delta X}$', size = 'larger')

# Valores ajustados a resíduos 
# Gerar os valores ajustados do modelo 
fitted = model.predict(dataframe[predictors])
# Calcular os resíduos 
residuals = dataframe[outcome] - fitted
# Exibir o Gráfico do correlação 
res = dataframe.plot.scatter(x = 'Exposure', y = 'PEFR', ax = res)
res.plot(dataframe.Exposure, fitted)
# Para cada vallor de índice 
for x, yatual, yfitted in zip(dataframe.Exposure, dataframe.PEFR, fitted):
    print(f'x: {x} - yreal: {yatual} - yreta: {yfitted}')
    res.plot((x, x), (yatual, yfitted), '--', color='C1')
print("-" * 250)

plt.tight_layout()
plt.show()