import pandas as pd
import numpy as np
import math

def analisar_dados_estatisticos(dados_brutos, nome_do_conjunto):
    print(f"-----Análise estatística para: {nome_do_conjunto}-----")
    
    
    # 1. Rol (Dados Ordenados)
    rol = sorted(dados_brutos)
    print("\n1. Rol (Dados Ordenados):")
    print(f" {rol}")
    
    # 2. Tamanho Amostra (n)
    n = len(rol)
    print("\n2. Tamanho da Amostra (n):")
    print(f" n = {n}")
    
    # 3. Valor Maximo e valor minimo

    x_min = rol[0]
    x_max = rol[-1]
    print("\n3. Valor minimo e maximo")
    print(f"valor min: {x_min}")
    print(f"valor max: {x_max}")
    
    #  4. Amplitude total (AT)
    at = x_max - x_min 
    print("\n4. Amplitude Total (AT): ")
    print(f" AT = {at:.2f}")
    
    # 5. Numero de classes 
    k = math.ceil(math.sqrt(n))
    print(f"\n5. Número de Classes (k): ")
    print(f"k = {k}")
    
    # 6. Amplitude  das classes (h)
    if at < 1:
        h = at / k
    else:
        h = math.ceil(at / k)
    
    print ("/n6. Amplitude das classes (k): ")
    print (f"h = {h}")
    
    classes = []
    frequencias_absolutas = []
    pontos_medios = []
    frequencias_relativas_dec = []
    frequencias_relativas_perc = []
    frequencias_absolutas_acum = []
    
    frequencia_abs_acum = 0
    limite_inferior = x_min
    for i in range(k): # k = 5 (numero de classes)
        limite_superior = limite_inferior + h 
        # Classes 
        classes.append(f"[{limite_inferior:.2f}--| {limite_superior:.2f}]")
        # Frequencias absolutas 
        if i == k - 1:
            frequencia_absoluta = len([x for x in rol if limite_inferior <= x <= limite_superior])
        else:
            frequencia_absoluta = len([x for x in rol if limite_inferior <= x < limite_superior])

        frequencias_absolutas.append(frequencia_absoluta)
        # Ponto medio das classes 
        pontos_medios.append((limite_inferior + limite_superior) / 2)
        # RELATIVA DECIMAL 
        frequencias_relativas_dec.append(frequencias_absolutas[i] / n)
        #Relativa Absoluta Acumyulada
        frequencia_abs_acum = frequencia_abs_acum + frequencias_absolutas[i]
        frequencias_absolutas_acum.append(frequencia_abs_acum)
        #Relativa percentual 
        frequencias_relativas_perc.append(frequencias_relativas_dec[i] * 100)
        limite_inferior = limite_superior
    
    df_frequencia = pd.DataFrame({
        'Classe': classes,
        'Ponto Medio' : pontos_medios,
        'Frequência Absoluta': frequencias_absolutas,
        'Frequência Relativa Decimal': frequencias_relativas_dec,
        'Frequência Relativa Percentual (%)': frequencias_relativas_perc,
        'Frequência Absoluta Acumulada': frequencias_absolutas_acum
    })
    
    df_frequencia.loc['Total'] = [
        'Total',
        np.nan,
        df_frequencia['Frequência Absoluta'].sum(),
        df_frequencia['Frequência Relativa Decimal'].sum(),
        df_frequencia['Frequência Relativa Percentual (%)'].sum(),
        np.nan
    ]
    return df_frequencia

    '''
    # Arredondar amplitude das classes
    num_casas_decimais = 0
    if at <k: #0.1
        num_casas_decimais = 1 
        if at * 10 < k: #0.01
            num_casas_decimais = 2
    h = np.ceil(h* (10**num_casas_decimais)) / (10**num_casas_decimais)
    print("\n6. Amplitude das classes (h): ")
    print(f"h = {int(h)}")
    '''

    
#----ESTUDO DE CASO 01: idade dos alunos
dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
df_idades = analisar_dados_estatisticos(dados_idades, "Idades dos Alunos")
print(df_idades.to_string(float_format="%.2f"))

# ----ESTUDO DE CASO 02: Tempo de atendimento em CALL CENTER
dados_call_center = [5.2, 8.1, 6.5, 12.0, 7.3, 5.8, 9.5, 11.2, 6.0, 7.8, 5.5, 10.1, 6.7, 7.0, 8.5, 13.5, 6.2, 7.5, 9.0, 10.5, 5.0, 8.8, 6.9, 7.2, 11.5, 6.3, 9.8, 10.0, 7.6, 8.0]
df_call_center = analisar_dados_estatisticos(dados_call_center, "Tempo de Atendimento em Call Center")
print(df_call_center.to_string(float_format="%.2f"))

# ----ESTUDO DE CASOS 3: Idaes de Bebes de uma Padaria 
dados_idades_bebes = [0.2, 0.9, 0.4, 0.7, 0.1, 0.8, 0.3, 0.6, 0.5, 0.2, 1.0, 0.7, 0.3, 0.9, 0.5, 0.1, 0.8, 0.4, 0.6, 1.0, 0.2, 0.7, 0.5, 0.9, 0.3]
df_idades_bebes = analisar_dados_estatisticos(dados_idades_bebes, "Idades de Bebes de uma Padaria")
print(df_idades_bebes.to_string(float_format="%.2f"))

print(df_idades.to_json(indent = 4, orient = 'records', force_ascii = False))