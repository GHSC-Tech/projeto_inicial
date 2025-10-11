
nome = input("Qual o seu nome:")
salario = float(input("Qual seu salário:"))
bonus = 1.5

bonus_total_recebido = salario * bonus + 1000

print("Ola " + nome +". Você tem " + str(len(nome)) + " no seu nome.")

print(f"Ola {nome}. Voê tem {len(nome)} letras no seu nome.")


print("O seu salário é: R$ " + str(salario) + " e o seu bônus foi de " + str(bonus_total_recebido) )