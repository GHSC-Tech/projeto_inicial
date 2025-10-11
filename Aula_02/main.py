#Lidando com erro em python
#Se fizer isso e não tiver faça aquilo, esse é o conceito básico de Try e Except
#Exemplo

# 4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
try:
    inf_div1 = int(input("Informe o primeiro número da divisão: "))
    inf_div2 = int(input("Informe o segundo número da divisão: "))
    result_div = inf_div1 // inf_div2
#Tipos de saída de erros
#Se o usuário tentar dividir por zero
except ZeroDivisionError:
    print("Intefer divisionor modulo by zero")
#Usuário pressionou uma tecla ao invés de digitar um núemro
except KeyboardInterrupt:
    print("Acho que você não quis inserir um número")


# Exemplo que causa TypeError

try:
    resultado = len(5)
    print(resultado)
except TypeError as e:
    print(e) #Imprime a mensagem de erro
#Caso esteja tudo correto, faça isso:
else:
    print("Tudo ocooreu bem")
#Independente do resultado
finally:
    print("O seu código foi finalizado")

#O isinstance avalia uma determinada coisa

numero = input("Insira um número: ")
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

#explicando if
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")