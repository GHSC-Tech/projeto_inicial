print("Jornada de dados")

# Variáveis
idade =  34
nome = "GUilherme"

#Print
print(idade)

#Soma
nova_idade = idade + 1
print(nova_idade)

#Lista
lista = [1,2,3,4,5]

#Métodos
list_invertida = lista.reverse()

import pandas as pd
import gzip
import os # Para manipulação de arquivos

# Criar dados simples (seu DataFrame)
data = {
    'id' [1, 2, 3],
    'nome' ['Ana Virginia', 'Carlos Augusto', 'Beatriz Clara'],
    'idade' ['28,22', '34,02', '22,23']
}
df = pd.DataFrame(data)

# 1. Salvar o DataFrame como um arquivo Excel (.xlsx) normal
excel_filename = 'teste_dados.xlsx'
df.to_excel(excel_filename, index=False)
print(fArquivo '{excel_filename}' criado com sucesso!)

# 2. Compactar o arquivo Excel criado com gzip
gzip_filename = 'teste_dados.xlsx.gz'
with open(excel_filename, 'rb') as f_in # Abre o Excel em modo binário de leitura
    with gzip.open(gzip_filename, 'wb') as f_out # Abre o arquivo gzip em modo binário de escrita
        f_out.writelines(f_in) # Copia o conteúdo do Excel para o arquivo gzip

print(fArquivo '{gzip_filename}' criado e o Excel compactado com sucesso!)

# Opcional Remover o arquivo Excel original se você só precisar da versão gzip
# os.remove(excel_filename)
# print(fArquivo '{excel_filename}' original removido.)