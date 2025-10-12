#divisão
print(5 / 4)

#divisão inteira
print(5 // 4)

#resto da divisão
print(6 % 4)

nome_aluno = 'Guilherme'

#tipos da variável
print(type(nome_aluno))
print(type('Gustavo'))

#conversão para maiúscula
print(nome_aluno.upper())

#conversão para minúsculas
print(nome_aluno.lower())

nome_aluno2="     Carlos"
#remover espaços em branco
print(nome_aluno2.split())

ex1="Casa-hotel"
print(ex1.split("-"))

# Exercícios
# Inteiros (int)
# 1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.
number_1=int(input("Digite o primeiro número: "))
number_2=int(input("Digie o segundo núemro inteiro: "))
resultado= number_1 + number_2
print(f'Ex01 - A soma é: {resultado}')

# 2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
inf_number= int(input("Informe um número: "))
result_info= (inf_number % 5)
print(f'Ex02 - O resultado do resto da divisão por 5 é: {result_info}')
# 3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
inf_mult1 = float(input("Informe o primeiro número da multiplicação: "))
inf_mult2 = float(input("Informe o segundo núemro da multiplicação: "))
result_mult= inf_mult1 * inf_mult2
print(f'Ex03 - O resultado da multificação é: {result_mult}')
# 4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
inf_div1 = int(input("Informe o primeiro número da divisão: "))
inf_div2 = int(input("Informe o segundo número da divisão: "))
result_div = inf_div1 // inf_div2
print(f'Ex04 - O resltado entre a divisão dos núemros {inf_div1} por {inf_div2} é: {result_div}')
# 5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
inf_quad =  int(input("Informe o número para o calculo do seu quadrado: "))
result_quad = inf_quad ** 2
print(f'Ex05 - O quadrado do número {inf_quad} é: {result_quad}')

# Números de Ponto Flutuante (float)
# 6-Escreva um programa que receba dois números flutuantes e realize sua adição.
inf_float1 = float(input("Informe o primeiro número: "))
inf_float2 = float(input("Informe o segundo número: "))
result_float = inf_float1 + inf_float2
print(f'Ex06 - O resultado é: {result_float}')
# 7-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
inf_float1 = float(input("Informe o primeiro número: "))
inf_float2 = float(input("Informe o segundo número: "))
result_float = (inf_float1 + inf_float2)/2
print(f'Ex07 - O resultado é: {result_float}')
# 8-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
inf_base1 = int(input("Informe o primeiro número base: "))
inf_exp1 = int(input("Informe o primeiro número expoente: "))
result_pont = inf_base1 ** inf_exp1 
print(f'Ex08 - O resultado é: {result_pont}')
# 9-Faça um programa que converta a temperatura de Celsius para Fahrenheit.
inf_cel1= float(input("Informe a temperatura em Celsius "))
result_fahrenheit = (inf_cel1 * 9/5) + 32
print(f"Ex09 - A temperatura convertida de graus Celsius de {inf_cel1}°C para Fahrenheit é: {result_fahrenheit}°F")
# 10-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
inf_circle = float(input("Informe o raio: "))
result_circle = math.pi * inf_circle ** 2
area_format = "{:.2f}".format(result_circle)
print(f"Ex10 - A área do círculo é: {area_format}")
# forma mais recente de usar
print(f"Ex10 - A área do círculo é: {result_circle:.2f}")

# Strings (str)
# 11-Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
text = str(input("Qual o texto a ser informado: "))
print(text.upper())
# 12-Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
text = str(input("Qual o seu nome completo: "))
print(text.lower())
# 13-Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
text = str(input("Informe uma frase: "))
print(text.strip())
# 14-Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
inf_date = input("Informe uma data de acordo com o padrão dd/mm/aaaa: ")
list_date = inf_date.split("/")
print(f'Ex14 - O dia é: {list_date[0]}, o mês: {list_date[1]} e o ano {list_date[2]}')
# 15-Escreva um programa que concatene duas strings fornecidas pelo usuário.
text_1 = str(input("Qual o primeiro texto:"))
text_2 = str(input("Qual o segundo texto:"))
uni_text = text_1 + text_2
print(uni_text)

# Booleanos (bool)
# 16-Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def avaliar_boleano(prompt):
    """
    Função auxiliar para garantir que a entrada do usuário seja um booleano
    """
    while True:
        entrada = input(prompt).strip().lower()
        if entrada == 'true':
            return True
        elif entrada == 'false':
            return False
        else:
            print("Entrda inválida. Por favor, digite 'True' ou 'False'.")
# 1. Obter as duas entradas booleanas do usuário
print("--- Avaliação de Expressões Booleanas (AND) ---")
valor1 = avaliar_boleano("Informe o valor da PRIMEIRA expressão (True/False): ")
valor2 = avaliar_boleano("Informe o valor da SEGUNDA expressão (True/False): ")
# 2. Aplicar a operação lógica AND
resultado_and = valor1 and valor2
# 3. Imprimir o resultado
print("\n--- Resultado da Operação Lógica ---")
print(f"Primeira expressão (A): {valor1}")
print(f"Segunda expressão (B):  {valor2}")
print("-" * 5)
print(f"Resultado de A AND B:    {resultado_and}")


# 17-Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def booleano_or(prompt):
    """
    Função auxiliar para garantir que a entrada do usuário seja um booleano
    """
    while True:
        entrada = input(prompt).strip().lower()
        if entrada == 'true':
            return True
        elif entrada == 'false':
            return False
        else:
            print("Entrada inválida. Por favro, digite 'True' ou 'False'.")
# 1. Obter as duas entradas booleanas do usuário
print("--- Avaliação de Expressões Booleanas (OR) ---")
valor1 = booleano_or("Informe o valor da PRIMEIRA expressão (True/False): ")
valor2 = booleano_or("Informe o valor da PRIMEIRA expressão (True/False): ")
# 2. Aplicar a operação lógica OR
resultado_or = valor1 or valor2
# 3. Imprimir o resultado
print("\n--- Resultado da Operação Lógica ---")
print(f"Primeira expressão (A): {valor1}")
print(f"Segunda expressão (B):  {valor2}")
print("-" * 5)
print(f"Resultado de A OR B:    {resultado_or}")

# 18-Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def invert_booleano(prompt):
    """
    Função para avaliar um valor booleano e inverte o seu valor
    """
    while True:
        entrada = input(prompt).strip().lower()
        if entrada == 'true':
            return False
        elif entrada == 'false':
            return True
        else:
            print("Entrada inválida. Por favro, digite 'True' ou 'False'.")
# 1. Obter as duas entradas booleanas do usuário
print("--- Avaliação de Expressões Booleanas (OR) ---")
valor1 = invert_booleano("Informe o valor da PRIMEIRA expressão (True/False): ")
valor2 = invert_booleano("Informe o valor da PRIMEIRA expressão (True/False): ")
# 2. Aplicar a operação lógica OR
resultado_or = valor1 or valor2
# 3. Imprimir o resultado
print("\n--- Resultado da Operação Invertida ---")
print(f"Primeira expressão (A): {valor1}")
print(f"Segunda expressão (B):  {valor2}")

            
# 19-Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print("--- Informe os dois valores de comparação")
valor1 = int(input("Informe o valor da primeira expressão: "))
valor2 = int(input("Informe o valor da primeira expressão: "))
avaliar = valor1 == valor2
print("\n--- Resultado da Operação Invertida ---")
print(f"Primeiro valor (A): {valor1}")
print(f"Segunda valor (B):  {valor2}")
print("-" * 5)
print(f"Resultado da avaliação:    {avaliar}")

# 20-Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print("--- Informe os dois valores de comparação")
valor1 = int(input("Informe o valor da primeira expressão: "))
valor2 = int(input("Informe o valor da primeira expressão: "))
avaliar = valor1 != valor2
print("\n--- Resultado da Operação Invertida ---")
print(f"Primeiro valor (A): {valor1}")
print(f"Segunda valor (B):  {valor2}")
print("-" * 5)
print(f"Resultado da avaliação:   {avaliar}")

# try-except e if
# 21 - Conversor de Temperatura - Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
#  O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    #Código para solicitar a entrada e tentar a conversão
    celsius_str = input("Digite a temperatura em Celsius: ")
    temperatura_celsius = float(celsius_str) #Tenta a conversão, pode gerar ValueError

    # Conversão de C para F: F = (C * 9/5) + 32
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
except ValueError:
    #Código para tratar o erro de entrada não numérica
    print("\nErro: A entrada não é válida. Por favor, digite um valor numérico para a temperatura.")
else:
    # Usando f-string e formatando para duas casas decimais para clareza
    print(f"\nA temperatura de {temperatura_celsius:.2f}°C equivale a {temperatura_fahrenheit:.2f}°F.")

# 22 - Verificador de Palíndromo - Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
#  Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

try:
    #Código para solicitar o texto a ser avaliado
    texto_entrada = input("Digite o texto em palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações): ").strip()

    #Validação de tipo
    if not isinstance(texto_entrada, str):
        pass
    
    #Limpar o texto para a verificação do palíndromo
    texto_limpo = ''.join(char.lower() for char in texto_entrada if char.isalnum())
except Exception as e:
    #Trata qualquer erro inesperado durante a leiura/limpeza
    print(f"Ocooreu um erro na leitura do texto: {e}")
    
else:
    #Verifica Palíndmo
    texto_reverso = texto_limpo[::-1]

    if texto_limpo == texto_reverso and texto_limpo != "":
        print(f"\nResultado: O texto '{texto_entrada}' É um palíndromo!")
    elif texto_limpo == "":
        print("\nResultado: Você não digitou caracteres válidos para avaliação.")
    else:
        print(f"\nResultado: O texto '{texto_entrada}' NÃO é um palíndromo.")


# 23 - Calculadora Simples - Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas.
#  Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    #Informando os numeros para serem calculados
    num_1 = float(input("Informe o primeiro número: "))
    num_2 = float(input("Informe o segundo número: "))
    operador = input("Informe qual o tipo do operador do calculo (+, -, *, /): ").strip()
    result = None #Inicializa o resultado

    if  operador != '/' and num_2 != 0 :
        pass

except ValueError:
    #Trata qualquer erro inesperado durante a leiura
    print("\nErro: Entrada não numérica. Certifique-se de digitar números válidos.")

else:
    # Usar if-elif-else sequencial

    if operador == '+':
        result = num_1 + num_2
    elif operador == '-':
        result = num_1 - num_2
    elif operador == '*':
        result = num_1 * num_2

    #Tratamento específico da Divisão por Zero
    elif operador == '/': 
        try:
            result = num_1 / num_2
        except ZeroDivisionError:
            print("\nErro: Divisão por zero não permitida.")
            # Define result como None para não imprimir a mensagem final de sucesso
            result = None 
    #Tratamento de operador inválido        
    else:
        print("\nErro: Operador inválido. Use apenas +, -, *, ou /.")

    # Imprimir o Resultado (Se o cálculo foi bem-sucedido)
    if result is not None:
        print(f"\nO resultado do cálculo entre os numeros {num_1} {operador} {num_2} é: {result:.2f}")


# 24 - Classificador de Números - Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero".
#  Adicionalmente, identifique se o número é "par" ou "ímpar".





# 25 - Conversão de Tipo com Validação - Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.