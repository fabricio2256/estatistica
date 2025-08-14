import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  r2_score, mean_squared_error

HOUSE_CSV = '../data/house_sales.csv'
df_house = pd.read_csv(HOUSE_CSV, sep='\t')

predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
outcome = 'AdjSalePrice'
print("-" * 250)
print(df_house[predictors].head())
print("-" * 250)
print(df_house[outcome].head())
print("-" * 250)

# Instancia do medelo de regressão linear 
house_lm = LinearRegression()
# Treinar o modelo, processo de ajuste
house_lm.fit(df_house[predictors], df_house[outcome])

print(f'Intercepto: {house_lm.intercept_:.3f}')
print("-" * 250)
print('Coeficientes')
for name, coef in zip(predictors, house_lm.coef_):
    print(f'{name}: {coef}')
print("-" * 250)

# AVALIAR A QUALIDADE DO MODELO 
fitted = house_lm.predict(df_house[predictors])
# RMSE (Root Mean Squared Error)
# é uma  medida da magnitude dos erros entre os valores previstos 
RMSE = np.sqrt(mean_squared_error(df_house[outcome], fitted))
r2 = r2_score(df_house[outcome], fitted)
print(f'RMSE: {RMSE:.0f}')
print("-" * 250)
print(f'r2: {r2:.4f}')
print("-" * 250)

std_dev = np.std(df_house['AdjSalePrice'])
print(f'Desvio padrão de AdjSalePrice: {std_dev:.2f}')
print("-" * 250)
rmse_percentual = (RMSE / np.mean(df_house['AdjSalePrice'])) * 100
print(f'RMSE percentual: {rmse_percentual:.2f}')
print("-" * 250)