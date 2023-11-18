#Primeiro, vamos criar a função para cálcular os gastos com a diária do hotel
def gastos_hotel(dias):
  gastos = 150 * dias
  return gastos

#Agora, vamos criar a função para cálcular os gastos com o combustível
def gastos_combustivel(distancia):
  gasto_comb = 5 * (distancia/14)
  return gasto_comb

#Função responsável por cálcular os gastos em cada localidade
def gastos_passeio(custo_destino, dias):
  gasto_pas = dias * custo_destino
  return gasto_pas

custos_destinos = [200, 400, 250, 300] #Salvador, Fortaleza, Natal e Aracaju
distancia_destinos = [850, 800, 300, 550]

#Criando um dicionário para associar os custos, distancias de Recife ate o destino e os nomes dos destinos
destinos = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
informacoes_destinos = {}

for i in range(len(destinos)):
  informacoes_destinos[destinos[i]] = {
      'custos': custos_destinos[i],
      'distancia': distancia_destinos[i]
  }

destino_requerido = input('Ola, digite a cidade que você deseja visitar:')
destino_requerido = destino_requerido.lower()
destino_requerido = destino_requerido.capitalize()

#FOR para armazenar o custo e a distancia do destino desejado
for i in range(len(informacoes_destinos)):
  if destino_requerido == destinos[i]:
    custos = informacoes_destinos[destinos[i]]['custos']
    distancia = informacoes_destinos[destinos[i]]['distancia']
    dias = int(input('Destino Encontrado! Agora, digite o numero de dias que você deseja ficar hospedado: '))

    #Agora, com os custos e a distancia do destino encontrados, basta chamar as funções.
    gastos = gastos_hotel(dias)
    gastos += gastos_combustivel(distancia)
    gastos += gastos_passeio (custos, dias)
    print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {destino_requerido} saindo de Recife custaria {gastos:.2f} reais")
    break