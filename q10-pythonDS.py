
frase = input('Olá, digite uma frase: ')
palavras = frase.split()

#Realizar o tratamento de caracteres especiais em cada palavra da lista
lista_aux = []
for palavra in palavras:
  palavra = palavra.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
  lista_aux.append(palavra)

palavras = lista_aux

#Filtrar a lista depois do tratamento apenas para palavras com 5 ou mais letras
palavras = list(filter(lambda word: len(word) >= 5, palavras))
print(palavras)