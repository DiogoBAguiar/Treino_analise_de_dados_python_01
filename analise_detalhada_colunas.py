import pandas as pd
# Esta linha lê o arquivo Excel e carrega os dados em um DataFrame do pandas. Resultado: Ele lê o cabeçalho incorretamente.
df = pd.read_excel(r'c:\Users\Diogo Bruno\OneDrive\Área de Trabalho\aprendendo-pyton\estudo_ciencia_de_dados\exercicio_01\default_of_credit_card_clients.xls')
# Promove a primeira linha para ser o cabeçalho correto.
#df.columns = df.iloc[0] seleciona a primeira linha do DataFrame
df.columns = df.iloc[0]
#------------------------------------------------------
#remove a primeira linha do DataFrame original, que agora é redundante
df = df.drop(df.index[0])
#este comando redefine os índices do DataFrame para começar de 0 novamente(0, 1, 2, ...)
df = df.reset_index(drop=True)
print("DataFrame com cabeçalho corrigido:")
print(df.head())
print("\nNovas informações das colunas:")
df.info()