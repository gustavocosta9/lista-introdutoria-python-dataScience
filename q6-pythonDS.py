def lista():
  notas = []
  for i in range(5):
    notas.append(float(input(f'Digite a {i+1} nota: ')))
  return notas

lista_2 = lista()

def operacoes(lista):
  maior_nota = max(lista_2)
  menor_nota = min(lista_2)
  media = sum(lista_2)/len(lista_2)
  if media >= 6:
    situacao = 'Aprovado(a)'
  else:
    situacao = 'Reprovado(a)'

  print(f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}')
