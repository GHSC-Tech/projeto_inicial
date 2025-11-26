import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários. 

    Docstring for ler_csv
    
    :param nome_do_arquivo_csv: Description
    :type nome_do_arquivo_csv: str
    :return: Description
    :rtype: list[dict]
    """

    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


#Teste para rodar a função

# vendas_itens: list[dict]

# vendas_itens = ler_csv(path_arquivo)
# print(vendas_itens)

def filtrar_produtos_de_uma_categoria(lista: list[dict]) -> list[dict]:
    """
    Docstring for filtrar_produtos_de_uma_categoria
    
    Função que filtra produtos da categoria Electronics

    :param lista: Description
    :type lista: list[dict]
    :return: Description
    :rtype: list[dict]
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("Categoria") == "Electronics":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

# lista_de_produtos = ler_csv(path_arquivo)
# produtos_electronics = filtrar_produtos_de_uma_categoria(lista_de_produtos)
# print(produtos_electronics)

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Docstring for somar_valores_dos_produtos

    Soma todos os produtos da categoria Electronics
    
    :param lista_com_produtos_filtrados: Description
    :type lista_com_produtos_filtrados: list[dict]
    :return: Description
    :rtype: int
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("Venda"))
    return valor_total

# lista_de_produtos = ler_csv(path_arquivo)
# produtos_electronics = filtrar_produtos_de_uma_categoria(lista_de_produtos)
# valor_dos_produtos_electronics = somar_valores_dos_produtos(produtos_electronics)
# print(valor_dos_produtos_electronics)