lista= list()
n=int(input('Quantidade de nomes quer inserir na lista :'))
for c in range(1,n+1):
    num=int(input('Nome que deja inserir '))
    lista.append(num)
print(lista)
som=0
max=lista[0]
mim=lista[0]
for i in lista:
    som += i
    if mim >= i:
        mim = i
    if max <= i:
        max = i

media = som/n
print(('SOMA {}').format(som))
print(('MEDIA: {}').format(media))
print(('MENOR: {}').format(mim))
print(('MAIOR: {}').format(max))