def verif_pontuacao(lista1, lista2):
  lista_concatenada = list(map(lambda gol_marc, gol_sofr: gol_marc - gol_sofr, lista1, lista2))

  #Agora que temos a lista com a comparação entre o valores marcados e sofridos, vamos percorre-la para calcular a pontuação
  pontuacao = 0
  for resultado in lista_concatenada:
    if resultado > 0:
      pontuacao +=3
    elif resultado == 0:
      pontuacao +=1

  pontuacao_max = len(lista1) * 3
  aproveitamento = (pontuacao / pontuacao_max) * 100

  print(f"A pontuação do time foi de {pontuacao} e seu aproveitamento foi de {aproveitamento:.2f}%")


gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

verif_pontuacao(gols_marcados, gols_sofridos)