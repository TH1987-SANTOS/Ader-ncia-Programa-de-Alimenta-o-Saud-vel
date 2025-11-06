import csv

# Contar produtos alimentícios por tipo
saudavel_count = 0
nao_saudavel_count = 0
total_alimenticios = 0
total_registros = 0

with open('clientes_programa_lealdade.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        total_registros += 1
        if row['Categoria_Preferida'] == 'Produtos Alimenticios':
            total_alimenticios += 1
            if row['Tipo_Produto'] == 'Saudavel':
                saudavel_count += 1
            elif row['Tipo_Produto'] == 'Não Saudavel':
                nao_saudavel_count += 1

print("=== RELATÓRIO DO DATASET ===")
print(f"Total de registros: {total_registros}")
print(f"Total de produtos alimentícios: {total_alimenticios}")
print(f"\nDistribuição de produtos alimentícios:")
print(f"Saudável: {saudavel_count} ({saudavel_count/total_alimenticios*100:.1f}%)")
print(f"Não Saudável: {nao_saudavel_count} ({nao_saudavel_count/total_alimenticios*100:.1f}%)")
print(f"\nPorcentagem de produtos alimentícios no dataset: {total_alimenticios/total_registros*100:.1f}%")
