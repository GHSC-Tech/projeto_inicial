### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = float(input("Informe a quantidade: "))
preco = float(input("Informe o preço: "))

if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa'(20 graus), 'Normal' (23 graus) ou 'Alta'(24 graus). Considerando que:

temperatura = float(input("Informe a temperatura atual do sensor: "))

if temperatura < 20:
    print("Baixa")
elif temperatura < 23:
    print("Normal")
else:
    print("Alta")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

import time

# Obter a data e hora atual no formato local
local_time = time.localtime()

# Formatando a data e hora
timestamp = time.strftime('%d/%m/%Y %H:%M:%S', local_time)

log =  {
    'timestamp': timestamp,
    'level': 'ERROR',
    'message': 'Falha na conexão'
}


# Exibir a mensagem de erro
if log['level'] == 'ERROR':
    print(log['timestamp'],log['message'])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Informe sua idade: "))
email = input("Informe seu e-mail: ")

erros = [] #Lista para armazenar os erros encontrados

#validação da idade
if idade < 18 or idade > 65:
    erros.append("Idade inválida (deve estar entre 18 e 65 anos).")

#validação e-mail
if "@" not in email or "." not in email.split("@")[-1]:
    erros.append("Email inválido (deve conter '@' e domínio válido, como exemplo@dominio.com).")

#resultado
if erros:
    for erro in erros:
        print(erro)
else:
    print("Dados de usuários válidos")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# Dado do exercício
transacao = {'valor':12000, 'hora': 20}

# Extraindo os dados
valor_transacao = transacao['valor']
horario_transacao = transacao['hora']

# Lista para armazenar motivos de suspeita
motivos_suspeita = []

# Verificação do valor
if valor_transacao > 10000:
    motivos_suspeita.append("Valor da transação é suspeito (acima de R$10.000)")

# Verificação o horário
if horario_transacao < 9 or horario_transacao > 18:
    motivos_suspeita.append("Horário da transação é suspeito (fora do horário comercial)")

# Resultado
if motivos_suspeita:
    print("Transação suspeita:")
    for motivo in motivos_suspeita:
        print(f"- {motivo}")
else:
    print("Transação válida")



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.


texto_de_entrada = input("Informe o texto para a avaliação de repetição: ")

texto_de_entrada = texto_de_entrada.lower()

palavras = texto_de_entrada.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print("\nContagem de palavras:")
for palavra, quantidade1 in contagem.items():
    print(f"{palavra}: {quantidade1}")


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Entrada do usuário
lista_entrada = input("Informe uma lista de valores para que seja normalizado (Os valores devem ser sepados por ','): ")

# Separar os valores com base na vírgula
lista_valores = lista_entrada.split(',')

# Converter cada item da lista de string para float
valores = [float(valor) for valor in lista_valores]

# Calcular o valor mínimo e máximo da lista
minimo = min(valores)
maximo = max(valores)

# Lista para armazenar os valores normalizados
valores_normalizados = []

# Aplicar a fórmula da normalização para cada valor
for valor in valores:
    normalizado = (valor - minimo) / (maximo - minimo)
    valores_normalizados.append(normalizado)

#Resultado
print("Valores normalizados:", valores_normalizados)


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@email.com"},
    {"nome": "Bob"},  # sem email
    {"nome": "Carol", "email": "carol@email.com"},
    {"nome": "", "email": "dan@email.com"},  # nome vazio
]

nome_vazio = []
email_vazio = []

for usuario in usuarios:
   # Se o nome estiver vazio, salva o email
   if usuario.get("nome", "") == "":
       nome_vazio.append(usuario["email"])

   # Se o email estiver vazio, salva o email
   if usuario.get("email", "") == "":
       email_vazio.append(usuario["nome"])

print("Emails de usuários com nome vazio:", nome_vazio)
print("Nomes de usuários com email vazio:", email_vazio)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Entrada do usuário
entrada = input("Informe uma lista de valores inteiros para definir aqueles que são pares (Usar como separador a vírgula ','): ")

# Converter cada item da lista de string para inteiros
numeros = [int(valor) for valor in entrada.split(',')]

# Lista para armazenar apenas os pares
lista_num_pares = []

# Verificar se cada número é par
for num in numeros:
    # Se o numero for par, salva na lista
    if num % 2 == 0:
        lista_num_pares.append(num)

#Resultado
print("Números pares:",lista_num_pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

registro_vendas = [
    {"categoria" : "bronze", "valor" : 1000},
    {"categoria" : "silver", "valor" : 750},
    {"categoria" : "gold", "valor" : 500},
    {"categoria" : "gold", "valor" : 200},
    {"categoria" : "bronze", "valor" : 100},
    {"categoria" : "silver", "valor" : 150}
]

# Dicionário acumulador
totais_por_categoria = {
    "bronze": 0,
    "silver": 0,
    "gold": 0
}

# Loop pelas vendas
for venda in registro_vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    totais_por_categoria[categoria] += valor

#Resultado
print(totais_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    entrada = input("Informe o texto (Quando quiser parar digite 'sair'): ").lower()
    if entrada == 'sair':
        break
    print(f"Você digitou: {entrada}")


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:
    
    try:
        numero = int(input("Informe um valor dentro do intervalo de 1 a 10 (ou 0 para sair): "))
        if numero == 0:
            print("Você saiu do programa, obrigado!")
            break
        elif numero >= 1 and numero <= 10:
            print("Número informado é válido.")
        else:
            print("Número informado é inválido.")
    
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
import requests

url = "https://brasilapi.com.br/api/ibge/uf/v1"
resposta = requests.get(url)

dados = resposta.json()  # Lista de dicionários

pagina = 0
tamanho_pagina = 5
total_dados = len(dados)

while True:
    inicio = pagina * tamanho_pagina
    fim = inicio + tamanho_pagina

    # Se não houver mais dados, encerra o loop
    if inicio >= total_dados:
        print("Não há mais páginas.")
        break

    pagina_dados = dados[inicio:fim]

    print(f"\n📄 Página {pagina + 1}")
    for estado in pagina_dados:
        print(f"{estado['sigla']} - {estado['nome']} ({estado['regiao']['nome']})")

    pagina += 1


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

import random

# Declarando os parâmetros

contador_tentativas = 0
limite_tentativas = 5
conectado = False # Status para identificar que ainda não existe conexação

while contador_tentativas < limite_tentativas and not conectado:
    contador_tentativas += 1
    print("Tentando conectar... (tentativa {contador_tentativas})")

    #Simula o sucesso da conexão 50% de chance a cada tentativa.
    conectado = random.choice([True, False])

    if conectado:
        print("Conexão bem-sucedida!")
    else:
        print("Falha na conexão. Tentando novamente...\n")
    
if not conectado:
    print("Número máximo de tentativas atingido. Conexão falhou.")



### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

#{}