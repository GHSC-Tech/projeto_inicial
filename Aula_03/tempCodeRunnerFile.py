lista_entrada = input("Informe uma lista de valores para que seja normalizado (Os valores devem ser sepados por ','): ")

lista_valores = lista_entrada.split(',')

valores = [float(valor) for valor in lista_valores]

minimo = min(valores)
maximo = max(valores)

valores_normalizados = []

for valor in valores:
    normalizado = (valor - minimo) / (maximo - minimo)
    valores_normalizados.append(normalizado)

print("Valores normalizados:", valores_normalizados)