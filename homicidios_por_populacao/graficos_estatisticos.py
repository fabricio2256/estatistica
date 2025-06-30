"""
Histograma:
     Gráfico de barras que representa uma distribuição de frequência.
     - Eixo x (horiz): intervalos (classes) dos dados
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
BoxPlot: 
     Diagrama de caixa que representa os extremos e mais os quartis
     - Min: O menor valor do conjunto de dados
     - Q1: Primeiro quartil dos dados (25%)
     - Q2: Segundo quartil dos dados, a mediana (50%)
     - Q3: Terceiro quartil dos dados (75%)
     - Max: O maior valor do conjunto de dados
Densidade:
     Gráfico que representa uma distribuição suavisada da frequência dos dados
     - Eixo x (horiz): intervalos (classes) dos dados
     - Eixo y (vertc): frequência (contagem) de itens por intervalo
Dispersão:
     Gráfico que representa a relação entre dois conjunto de dados
     - Eixos: Cada eixo representará um dos dois conjunto de dados
     - Pontos: Cada ponto representa a interseção entre as variáveis de ambos os conjuntos.

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import graficos_estatisticos

# Impromir o docstring
print(graficos_estatisticos)

# importa o csv
df_dados_brutos = pd.read_csv('taxa_homicidios.csv')

def histograma(): 
     bins_do_grafico = [2, 6, 9, 13]
     histograma = (df_dados_brutos['Taxa Homicídio']).plot.hist(figsize = (6, 4), bins = bins_do_grafico)
     histograma.set_xlabel('Taxa de Homicidios')
     histograma.set_ylabel('Freqência (Número de cidades)')
     plt.show()
     
def boxblot():
     boxblot = (df_dados_brutos['Taxa Homicídio']).plot.box()
     boxblot.set_ylabel('Taxa de homicídios') 
     plt.show()
     
def densidade():
     histograma = (df_dados_brutos['Taxa Homicídio']).plot.hist(density = True, bins = range(1, 16), figsize=(6,4))
     df_dados_brutos['Taxa Homicídio'].plot.density(ax = histograma)
     histograma.set_xlabel('Taxa de Homicídios')
     histograma.set_ylabel('Frequência (densidade)')
     plt.xlim(1, 15)
     plt.show()
     
def dispensao ():
     plt.figure(figsize=(10, 6))
     plt.scatter(df_dados_brutos["Taxa Homicídio"], df_dados_brutos["População"], alpha=0.7)
     plt.xlabel('População')
     plt.ylabel('Taxa Homicídio')
     plt.title('Gráfico de Dispensão: Taxa de homicídios vs população')
     plt.grid(True)
     plt.show()
     
# histograma()
# boxblot()
# densidade()
dispensao()