# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

# Solicita ao usuário que digite seu nome
nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
            #exit() dar saída do código
        # Verifica se há números no nome
        elif nome.isdigit():
        #elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
            #exit() dar saída do código
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)
        #exit() dar saída do código
# Solicita ao usuário que digite o valor do seu salário e converte para float

while salario_valido is not True:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True    
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        #exit() dar saída do código

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while bonus_valido is not True:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        #exit() dar saída do código

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

## DESAFIO PROF.GUANABARA

## 1 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
##Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

# Tupla com os números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    try:
        entrada = int(input("Digite um número entre 0 e 20: "))
        if entrada >= 0 and entrada <= 20:
            valor_extenso = isinstance(entrada, int)
            print(f'Você digitou o número {numeros[entrada]} ')
            
        else:
            print("Tente novamente. Digite um número entre 0 e 20: ")


    except ValueError:
        print("Entrada inválida para o valor solicitado. Por favor, digite um número.")

## 2 - Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
## a) Apenas os 5 primeiros colocados.
## b) Os últimos 4 colocados da tabela.
## c) Uma lista com os times em ordem alfabética.
## d) Em que posição na tabela está o time do Cruzeiro.

tabela_brasileiro = (
    'Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'Vasco da Gama', 'São Paulo', 'Bragantino','Corinthians',
      'Grêmio', 'Ceará SC', 'Internacional', 'Atlético-MG', 'Santos', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport Recife'
      )


print('-' * 50)
print("Resposta A")
for time in tabela_brasileiro[:5]:
    print(time)

print('-' * 50)
print("Resposta B")
for time in tabela_brasileiro[-4:]:
    print(time)

print('-' * 50)
print("Resposta C")
for time in sorted(tabela_brasileiro):
    print(time)

print('-' * 50)
print("Resposta D")
posicao_cruzeiro = tabela_brasileiro.index('Cruzeiro') + 1
print(f"O Cruzeiro está na {posicao_cruzeiro}ª posição da tabela.")


## 3 - Crie um programa que vai gerar cinco números aleatórios e colcoar em uma tuplas.
## Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10)
)


# Exibindo os números gerados
print("Os números sorteados foram: ", end="")
for n in numeros:
    print(f"{n} ", end="")

# Quebra de linha
print("\n")

# Exibindo o maior e o menor
print(f"O maior número sorteado foi: {max(numeros)}")
print(f"O menor número sorteado foi: {min(numeros)}")