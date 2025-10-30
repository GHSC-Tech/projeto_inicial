# Exercícios de Listas e Dicionários
# 1-Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# 1 - Solução

lista_numeros: int =  []

for elemento in range(1,11):
    print(f'\nMinha lista tem os seguintes números {elemento}.\n', end=" " )
    lista_numeros.append(elemento ** 2)

print("\nCada número foi elevado ao seu quadrado e o resultado seria esse:")
print(lista_numeros, end=" ")

# 2 - Solução

# Criando a lista com números de 1 a 10
lista_numeros: int = [element for element in range(1, 11)]

# Usando um loop para imprimir cada número elevado ao quadrado
for numero in lista_numeros:
    print(f'O número {numero} elevado ao quadrado é {numero ** 2}.')


# 2-Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# 1 - Solução

lista_itens: str = ["Python", "Java", "C++", "JavaScript"]

if "C++" in lista_itens:
    lista_itens.pop(2)
    lista_itens.append("Ruby")
else:
    print('"C++" não encontrado na lista.')

print(lista_itens)

# 2 - Solução

lista_itens: str = ["Python", "Java", "C++", "JavaScript"]

if "C++" in lista_itens:
    lista_itens.remove("C++")
    lista_itens.append("Ruby")
else:
    print('"C++" não encontrado na lista.')

print(lista_itens)


# 3-Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

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


# Imprime uma sequência dos elementos do dicionário..
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

# Defino um item do dicionário para imprimir
print(lista_de_livros_usando_dict["livro_01"])


# 4-Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

dicionario_ocorrencias: str = {}
entrada: str = input("Adicione um texto para ser avaliado: ")

for e in entrada:
    if e in dicionario_ocorrencias:
        dicionario_ocorrencias[e] += 1
    
    else:
        dicionario_ocorrencias[e] = 1
    
# Exibindo o resultado

print("Ocorrências de caracteres:")
for chave, valor in dicionario_ocorrencias.items():
    print(f"'{chave}': {valor}")


# 5-Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# 1 - Solução

from typing import Dict

produto_1: Dict[str, float] = {
    "Produto": "Maça",
    "Valor": 0.45   
}

produto_2: Dict[str, float] = {
    "Produto": "Banana",
    "Valor": 0.30   
}

produto_3: Dict[str, float] = {
    "Produto": "Cereja",
    "Valor": 0.65  
}

# Lista que contém os produtos comprados
lista_compras: list = [produto_1, produto_2, produto_3]

# Variável para armazenar o valor total da compra
valor_total: float = 0.0

# Iterando sobre cada item na lista de compras
for produto in lista_compras:
    # Verificando se o dicionário tem a chave 'Valor'
    if 'Valor' in produto:
        valor_total += produto['Valor']  # Somando o valor ao total da compra

# Exibindo o valor total
print(f"Valor total da compra: R${valor_total:.2f}")

# 2 - Solução

# Dicionário com os preços dos produtos
precos = {
    "maçã": 0.45,
    "banana": 0.30,
    "cereja": 0.65
}

# Lista de compras com os produtos desejados
lista_compras = ["maçã", "banana", "cereja"]

# Variável para armazenar o total da compra
total_compra = 0.0

# Percorrendo a lista de compras
for produto in lista_compras:
    # Somando o valor de cada produto ao total
    if produto in precos:
        total_compra += precos[produto]

# Exibindo o total
print(f"Total da compra: R${total_compra:.2f}")



# Exercícios intermediários e mais avançados

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# 1 - Solução

lista_emails: list[str] = [
    'claudio@gmail.com',
    'carlos@gmail.com',
    'breno@gmail.com',
    'carlos@gmail.com',
    'beatriz@gmail.com',
    'claudio@gmail.com',
]

lista_atualizada: list[str] = set(lista_emails)

print(lista_atualizada)

# 2 - Solução

lista_emails: list[str] = [
    'claudio@gmail.com',
    'carlos@gmail.com',
    'breno@gmail.com',
    'carlos@gmail.com',
    'beatriz@gmail.com',
    'claudio@gmail.com',
]

lista_atualizada: list[str] = []

for e_email in lista_emails:
    if e_email not in lista_atualizada:
        lista_atualizada.append(e_email)

print(lista_atualizada)


# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idade: str = input("Informe uma lista de idades separadas por vírgula: ")

lista_idade: list[int] = [int(x.strip()) for x in idade.split(',')]

idade_maior_18: list[int] = []

for idade in lista_idade:
    if idade >= 18:
        idade_maior_18.append(idade)

print(idade_maior_18)


# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# 1 - Solução

lista_nome: str = [
    "Augusto",
    "Bento",
    "Da Silva",
    "Wellington",
    "Bruno",
    "Carla"
]
lista_nome.sort()

print(lista_nome)

# 2 - Solução

pessoas: list[dict[str, int]] = [
    {"nome": "Augusto", "idade": 20},
    {"nome": "Bento", "idade": 25},
    {"nome": "Da Silva", "idade": 22},
    {"nome": "Wellington", "idade": 30},
    {"nome": "Bruno", "idade": 19},
    {"nome": "Carla", "idade": 28}
]

lista_ordenada: list[str] = sorted(pessoas, key=lambda pessoa: pessoa["nome"])

for pessoa in lista_ordenada:
    print(pessoa)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# Solicita a entrada de números
numeros: str = input("Informe uma lista de idades separadas por vírgula: ")

# Faz a conversão do tipo string para int
lista_numeros: list[int] = [int(x.strip()) for x in numeros.split(',')]

# Armazena o somatório da lista
total_numeros: int = 0

# Realiza a soma de cada item da lista
for num in lista_numeros:
    total_numeros += num

# Calcula a média
media: float = total_numeros / len(lista_numeros)

# Resultado
print(f"A média dos valores é: {media:.2f}")


# Iterando sobre cada item na lista de compras
for produto in lista_compras:
    # Verificando se o dicionário tem a chave 'Valor'
    if 'Valor' in produto:
        valor_total += produto['Valor']  # Somando o valor ao total da compra


# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.


#S olicita a entrada de números
numeros: str = input("Informe uma lista de idades separadas por vírgula: ")

# Faz a conversão do tipo string para int
lista_numeros: list[int] = [int(x.strip()) for x in numeros.split(',')]

lista_par = []
lista_impar = []

# Realiza a soma de cada item da lista
for num in lista_numeros:
    if num % 2 == 0 :
        lista_par.append(num)
        print(f'O número {num} foi adicionado a lista par.')
    else:
        lista_impar.append(num)
        print(f'O número {num} foi adicionado a lista ímpar.')

print("-"*50)
print(f'Os números da lista par são: {lista_par}')

print("-"*50)
print(f'Os números da lista ímpar são: {lista_impar}')

# Exercícios com Dicionários

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# 1 - Solução

from typing import Dict

produto_1: Dict[str, float] = {
    "Produto": "Maça",
    "Valor": 0.45   
}

produto_2: Dict[str, float] = {
    "Produto": "Banana",
    "Valor": 0.30   
}

produto_3: Dict[str, float] = {
    "Produto": "Cereja",
    "Valor": 0.65  
}

print(f' O antigo valor da Maçã era de : {produto_1["Valor"]}')

produto_1["Valor"] = 0.85

print(f' O novo valor da Maçã é : {produto_1["Valor"]}')



# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

from typing import Dict

produto_1: Dict[str, float] = {
    "Maça": 0.45   
}

produto_2: Dict[str, float] = {
    "Banana": 0.30   
}

novo_dicionário = {**produto_1, **produto_2}

print(novo_dicionário)


# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# 1 - Solução 

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

novo_estoque = []

for produto, quantidade in estoque.items():
     if quantidade > 0:
        novo_estoque.append((produto, quantidade))

print(novo_estoque)

# 2 - Solução 

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

hortifruti = {'laranja': 2, 'maçã': 3, 'pera': 4,  'banana': 1}

# Listas separadas
chaves = list(hortifruti.keys())
valores = list(hortifruti.values())

print("Lista de produtos:", chaves)
print("Lista de quantidades:", valores)

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"

novo_texto = texto.lower()

frequencia = {}

for contar in novo_texto:
    if contar in frequencia:
        frequencia[contar] += 1
    else:
        frequencia[contar] = 1
    
print(frequencia)


# Exercícios de Funções
# 16 - Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

numeros: list = [1, 2, 5, 8, 15, 38, 50, -20, 250]

def somar_numeros (numeros: list[int]) -> int:

    soma: int = 0

    for numero in numeros:
        soma += numero
    return soma


resultado = somar_numeros(numeros)

print(resultado)


# 17 - Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.


def testar_primo(n: int) -> bool:

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    
    for i in range(3, int(n**0.5)+ 1, 2):
        if n % i == 0:
            return False
    return True

avaliar_numero = int(input("Informe um numero para ser avaliado: "))

validar_numero = testar_primo(avaliar_numero)

print(f"{avaliar_numero} é primo? {validar_numero}")

# 18 - Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

# 19 - Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

# 20 - Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
