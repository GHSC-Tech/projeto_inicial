print("Esse é o primeiro comando") 
print("Esse é o segundo comando") 
print("Esse é o terceiro comando") 

# Variável simples
#e.g. 

lanche = 'pudim'

# Variável composta - Pode guarda vários valores.
#e.g.

minha_tupla = ('hambúrguer', 'suco', 'pizza', 'pudim')

#Quantidade de itens dentro da tupla
print(len(minha_tupla))

print("-" * 50)

#Fornecer o nome de cada iten da tupla
for c in minha_tupla:
    print(c)

print("-" * 50)

#Tipos de fatiamento da tupla
print(minha_tupla[1:3])
print(minha_tupla[2:])
print(minha_tupla[:2])
print(minha_tupla[-2])
print(minha_tupla[-3:])

print("-" * 50)

#Combinando for com tupla
for comida in minha_tupla:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print("-" * 50)

#Mostra a posição de cada elemento dentro da tupla -  Primeira Versão
for pos, comida in enumerate(minha_tupla):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')


print("-" * 50)

#Variação de for com range + len
for cont in range(0, len(minha_tupla)):
    print(f'Eu vou comer {minha_tupla[cont]}')


print("-" * 50)

#Mostra a posição de cada elemento dentro da tupla -  Segunda Versão
for cont in range(0, len(minha_tupla)):
    print(f'Eu vou comer {minha_tupla[cont]} na posição {cont}')


print("-" * 50)

#Coloca a tupla em ordem, nesse caso o Python cria uma lista para se fazer a ordenação.
print(sorted(minha_tupla))

print("-" * 50)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))#Conta as repetições do elemento
print(c.index(2)) #Retorna o elemento da segunda posição
print(c.index(5, 1)) # Retorna a posição do elemento após a posição 0
