import pandas as pd
import numpy as np

# Carregar o dataset
df = pd.read_csv('clientes_programa_lealdade.csv')

print("=== ANÁLISE CIENTÍFICA DO DATASET ===\n")

# 1. Características gerais
print("1. CARACTERÍSTICAS GERAIS:")
print(f"   • Total de observações: {len(df):,}")
print(f"   • Número de variáveis: {len(df.columns)}")
print(f"   • Período de coleta: Não especificado")
print(f"   • Unidade de análise: Cliente individual\n")

# 2. Estrutura das variáveis
print("2. ESTRUTURA DAS VARIÁVEIS:")
for col in df.columns:
    dtype = df[col].dtype
    unique_vals = df[col].nunique()
    missing = df[col].isnull().sum()
    print(f"   • {col}: {dtype} ({unique_vals} valores únicos, {missing} valores ausentes)")
print()

# 3. Variáveis categóricas
print("3. DISTRIBUIÇÃO DAS VARIÁVEIS CATEGÓRICAS:")
categorical_vars = ['Gênero', 'Cidade', 'Categoria_Preferida', 'Participa_Programa', 
                   'Feedback_Cliente', 'Canal_Preferred', 'Tipo_Produto']

for var in categorical_vars:
    if var in df.columns:
        print(f"   {var}:")
        dist = df[var].value_counts()
        for value, count in dist.items():
            pct = (count/len(df))*100
            print(f"      - {value}: {count} ({pct:.1f}%)")
        print()

# 4. Variáveis numéricas
print("4. ESTATÍSTICAS DESCRITIVAS DAS VARIÁVEIS NUMÉRICAS:")
numeric_vars = ['Idade', 'Renda_Anual (R$)', 'Frequência_Compra', 
               'Valor_Médio_Compra (R$)', 'Pontuação_Lealdade']

for var in numeric_vars:
    if var in df.columns:
        print(f"   {var}:")
        print(f"      - Média: {df[var].mean():.2f}")
        print(f"      - Mediana: {df[var].median():.2f}")
        print(f"      - Desvio padrão: {df[var].std():.2f}")
        print(f"      - Mínimo: {df[var].min():.2f}")
        print(f"      - Máximo: {df[var].max():.2f}")
        print(f"      - Quartil 25%: {df[var].quantile(0.25):.2f}")
        print(f"      - Quartil 75%: {df[var].quantile(0.75):.2f}")
        print()

# 5. Análise da variável dependente
print("5. ANÁLISE DA VARIÁVEL DEPENDENTE (Participa_Programa):")
target_dist = df['Participa_Programa'].value_counts()
for value, count in target_dist.items():
    pct = (count/len(df))*100
    print(f"   • {value}: {count} ({pct:.1f}%)")

print(f"\n   • Taxa de participação no programa: {(target_dist['Sim']/len(df))*100:.1f}%")
print()

# 6. Produtos alimentícios
if 'Tipo_Produto' in df.columns:
    alimenticios = df[df['Categoria_Preferida'] == 'Produtos Alimenticios']
    print("6. ANÁLISE ESPECÍFICA - PRODUTOS ALIMENTÍCIOS:")
    print(f"   • Total de clientes com preferência alimentícia: {len(alimenticios)} ({(len(alimenticios)/len(df))*100:.1f}%)")
    
    tipo_dist = alimenticios['Tipo_Produto'].value_counts()
    for tipo, count in tipo_dist.items():
        pct = (count/len(alimenticios))*100
        print(f"   • {tipo}: {count} ({pct:.1f}%)")
    
    # Participação por tipo de produto alimentício
    print("\n   Participação no programa por tipo de produto alimentício:")
    for tipo in ['Saudavel', 'Não Saudavel']:
        subset = alimenticios[alimenticios['Tipo_Produto'] == tipo]
        if len(subset) > 0:
            participa = subset['Participa_Programa'].value_counts()
            sim_pct = (participa.get('Sim', 0) / len(subset)) * 100
            print(f"      - {tipo}: {sim_pct:.1f}% participam do programa")
