# O método append adiciona um elemnto por vez e de forma única. Já o método extend, desconsidera o seu iterável  - (), [], {} - para adicionar os elementos de forma individual dentro da lista original.

produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)


numeros = []
numeros.extend(range(0,5))
print(numeros)


# Estrutura de lista

from typing import Dict, Any
produto_01: Dict[str, Any]

import json

lista: list = ["Sapato", 39, 10.38, True]


produto_01: Dict[str, Any] = {
    "nome" : "Sapato",
    "quantidade" : 39,
    "preco" : 10.38,
    "disponibilidade" : True
}

produto_02: dict = {
    "nome" : "Televisao",
    "quantidade" : 10,
    "preco" : 70.38,
    "disponibilidade" : False
}


carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)

