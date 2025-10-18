import pandas as pd
import gzip

# Criar dados simples
data = {
    'id': [1, 2, 3],
    'nome': ['Ana Virginia', 'Carlos Augusto', 'Beatriz Clara'],
    'idade': ['28,22', '34,02', '22,23']
}
df = pd.DataFrame(data)

# Salvar como arquivo .csv comprimido com gzip
with gzip.open('teste_dados.csv.gz', 'wt', encoding='utf-8') as f:
    df.to_xls(f, index=False)

print("Arquivo 'teste_dados.csv.gz' criado com sucesso!")