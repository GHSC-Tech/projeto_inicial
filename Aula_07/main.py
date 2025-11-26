from etl import ler_csv, filtrar_produtos_de_uma_categoria, somar_valores_dos_produtos

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_electronics = filtrar_produtos_de_uma_categoria(lista_de_produtos)
valor_dos_produtos_electronics = somar_valores_dos_produtos(produtos_electronics)
print(valor_dos_produtos_electronics)