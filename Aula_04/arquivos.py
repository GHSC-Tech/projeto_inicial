import csv

# Caminho para o arquivo CSV
path: str = "exempl.csv"

# Inicializa uma lista vazia para armazenar os dados
arquivo_csv: list = []

# Usa o gerenciador de contexto 'with' para abrir o arquivo.

with open(file=path, mode="r", encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)