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