import pandas as pd

df = pd.read_excel(r'c:\Users\Diogo Bruno\OneDrive\Área de Trabalho\aprendendo-pyton\estudo_ciencia_de_dados\exercicio_01\default_of_credit_card_clients.xls')

print(f"O dataset tem {df.shape[0]} linhas e {df.shape[1]} colunas.")
print(df.head())
