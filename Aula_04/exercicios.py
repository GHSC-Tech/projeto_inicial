# Exercícios de Listas e Dicionários
# 1-Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# 2-Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# 3-Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.


# Crie um dicionário para armazenar informações de um livro,
# incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2005
}

livro_02: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2007
}

lista_de_livros: list = []

lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)


# Imprimi uma lista sequência dos elementos do dicionário.
for livro in lista_de_livros:
    for chave, valor in livro.items():
        print(f"{chave}: {valor}")


# Fazendo um dicionário com vários elementos

lista_de_livros_usando_dict: dict = {
    "livro_01": {"Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2005},

    "livro_02": {"Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2007}
}

# Defini um item do dicionário para imprimir
print(lista_de_livros_usando_dict["livro_01"])




# 4-Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5-Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# Exercícios intermediários e mais avançados

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# Exercícios com Dicionários

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.


 #{}