from interface.classes.csv_class import CsvProcessor
#import pandas as pd

arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv() #Load the CSV
print(arquivo_CSV.filtrar_por(['estado', 'preco'], ['SP', '10,50']))


#Contexto de aplicação de filtro para colunas específicas
# print(arquivo_CSV.filtrar_por(filtro, limite))
# print(arquivo_CSV.sub_filtro('preco', '10,50'))
#print(arquivo_CSV.df)
print("###################################")
# arquivo_csv_2 = './exemplo2.csv'
# filtro_2 = 'estado'
# limite_2 = 'DF'

# arquivo_CSV_2 = CsvProcessor(arquivo_csv_2)
# arquivo_CSV_2.carregar_csv()
# print(arquivo_CSV_2.filtrar_por(filtro_2, limite_2))