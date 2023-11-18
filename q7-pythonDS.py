#Primeiramente, vamos tratar os caracteres escritos de forma incorreta.
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

def tratar_nomes(lista):
  lista_tratada = []
  for string in lista:
    string = string.lower()
    string = string.capitalize()
    lista_tratada.append(string)

  lista = lista_tratada
  return lista

nomes = tratar_nomes(nomes)
sobrenomes = tratar_nomes(sobrenomes)

#Agora, precisamos unir os nomes das duas listas diferentes, respectivamente.
def unir_nomes(lista1, lista2):
  lista_completa =  list((map(lambda nome1, nome2: nome1 + " " + nome2, lista1, lista2))) #Map é basicamente: map(ação, alvo)
  return lista_completa

nomes_completos = unir_nomes(nomes, sobrenomes)
print(nomes_completos)