# venv\Script\activate --- Ativa o ambiente venv ---

import pandas as pd
from faker import Faker
import random 

# gerador_ficticio=Fakrte('pt_BR')
fake = Faker('en_US')

# função para gerar dataframe 
def gerar_dados_brutos(hum_registro):
    dados_brutos = []
    lista_cidades = set()
    
    while len(dados_brutos) < num_registro:
        nome_cidade = fake.city()
        if nome_cidade not in lista_cidades :
            lista_cidades.add(nome_cidade)
            # gerar populção aleatória entre 10k e 5mi
            populacao = fake.random_int(min=1000, max=5000000)
            # gerar taxa de homicídios entre 1.0 e 15.0 arredondado e com uma casa decimal
            taxa_homicidios = round(random.uniform(1.0 , 15.0), 1)
            # Cruiação tabela DataFramer
            dados_brutos.append({
                "Cidade" : nome_cidade,
                "População" : populacao,
                "Taxa Homicídio" : taxa_homicidios
            })
    #Criação alimentada do DataFrame 
    return pd.DataFrame(dados_brutos)
    
num_registro = 10
df = gerar_dados_brutos(num_registro)
print("DataFrame gerado")
print(df)

output_csv_file = 'taxa_homicidios.csv'
df.to_csv(output_csv_file, index=False)
