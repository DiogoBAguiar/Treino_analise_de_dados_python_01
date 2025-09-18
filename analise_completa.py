import pandas as pd

df = pd.read_excel(r'c:\Users\Diogo Bruno\OneDrive\Área de Trabalho\aprendendo-pyton\estudo_ciencia_de_dados\exercicio_01\default_of_credit_card_clients.xls', header=None, skiprows=1)
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df = df.reset_index(drop=True)

colunas_para_converter = [
    'LIMIT_BAL', 'AGE',
    'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
    'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
]

for coluna in colunas_para_converter:
    df[coluna] = pd.to_numeric(df[coluna])

print("DataFrame carregado, corrigido e com tipos convertidos! Iniciando a descoberta!")
print("\n" + "="*50)
print("ETAPA 1: DESCOBRINDO OS TIPOS DE COLUNAS")
print("="*50)

colunas_numericas_inicial = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
colunas_categoricas_inicial = df.select_dtypes(include=['object']).columns.tolist()
if 'ID' in colunas_numericas_inicial:
    colunas_numericas_inicial.remove('ID')
print(f"\nDetectadas {len(colunas_numericas_inicial)} colunas numéricas inicialmente.")
print(f"Detectadas {len(colunas_categoricas_inicial)} colunas categóricas inicialmente.")
print("\n" + "="*50)
print("ETAPA 2: REFINANDO A CLASSIFICAÇÃO DAS COLUNAS")
print("="*50)
print("\nAnalisando colunas numéricas para encontrar 'falsas numéricas' (categóricas escondidas)...")

colunas_para_mover = []
for coluna in colunas_numericas_inicial:
    num_unicos = df[coluna].nunique()
    if num_unicos < 10:
        colunas_para_mover.append(coluna)
        print(f" -> A coluna '{coluna}' tem apenas {num_unicos} valores únicos. Será tratada como CATEGÓRICA.")

colunas_categoricas_final = colunas_categoricas_inicial + colunas_para_mover
colunas_numericas_final = [col for col in colunas_numericas_inicial if col not in colunas_para_mover]

print("\n--- Classificação Final ---")
print(f"Colunas Numéricas Finais: {colunas_numericas_final}")
print(f"Colunas Categóricas Finais: {colunas_categoricas_final}")

print("\n" + "="*50)
print("ETAPA 3: EXECUTANDO A ANÁLISE AUTOMÁTICA")
print("="*50)

print("\n--- Resumo Estatístico das Colunas NUMÉRICAS Descobertas ---")
print(df[colunas_numericas_final].describe().T)

print("\n--- Contagem de Frequência das Colunas CATEGÓRICAS Descobertas ---")
for coluna in colunas_categoricas_final:
    print(f"\n--- Contagem para a coluna: {coluna} ---")
    print(df[coluna].value_counts())

print("\n--- Verificação de Dados Faltantes ---")
if df.isnull().sum().sum() == 0:
    print("Ótima notícia: Não há dados faltando no dataset!")
else:
    print(f"Atenção: Há um total de {df.isnull().sum().sum()} células com dados faltantes.")