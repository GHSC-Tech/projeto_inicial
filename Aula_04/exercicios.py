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




 {}
