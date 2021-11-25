repet = {}
lista = list()
nome = '-'
while nome != '':
    nome = str(input('Insira um nome: '))
    lista.append(nome)
lista.remove('')
for nome in lista:
    if nome in repet:
        repet[nome] += 1
    else:
        repet[nome] = 1
print(repet)