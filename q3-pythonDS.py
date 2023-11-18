lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# Usando filter para filtrar apenas os valores da lista original que são multiplos de 3
lista_multiplos = list(filter(lambda x: x % 3 == 0, lista))

print(lista_multiplos)
