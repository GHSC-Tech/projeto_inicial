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


##-------Lista-Part_1---------

lanches = ['hambúrguer', 'suco', 'pizza', 'pudim']

#Opções para remover um item de uma lista
del lanches[3] # remove o pudim da lista
lanches.pop(3)
lanches.remove('pudim')


#Metódo para eliminar só aquilo que estiver dentro da lista
if 'café' in lanches:
    lanches.remove('café')

print(lanches)


valores = [8,2,5,4,9,3,0]
valores.sort() #Ordena os valores de uma lista, do menor para o maior
valores.sort(reverse=True) #Ordena os valores de uma lista, do maior para o menor
len(valores) #retorna a quantidade de elementos da lista
valores.insert(2,0) #Insere um numero na lista, defini a posição desejada. (índice,valor)
valores.pop()#remove o último elemento da lista.Para remover um elemento em uma posição específica, você precisa passar o índice como argumento 

a = [2,3,4,7]
b = a[:] #Copia a lista inteira de A para a variável B
b[2] = 8 #Na lista B, troca o elemento do índice 2 por 8.
print(f'Lista A: {a}')
print(f'Lista A: {b}')


#{}

