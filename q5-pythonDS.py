def lista():
  notas = []
  for i in range(5):
    notas.append(float(input(f'Digite a {i+1} nota: ')))
  return notas

def eliminacao(lista):
  maior = lista.index(max(lista))
  menor = lista.index(min(lista))

  #Agora, remover o maior e menor elemento da lista
  lista.pop(maior)
  lista.pop(menor)

  return lista

lista = lista()

lista = eliminacao(lista)
media = lambda lista: sum(lista)/len(lista)
media = media(lista)
print(f'Nota da manobra: {media}')