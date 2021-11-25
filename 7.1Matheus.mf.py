repet={}
lista= list()
n=int(input('Quantidade de nomes quer inserir na lista :'))
for c in range(1,n+1):
    nome=str(input('Nome que deja inserir '))
    lista.append(nome)
print(lista)
for nome in lista:
    if nome in repet:
        repet[nome] += 1
    else:
        repet[nome] = 1
print(repet)