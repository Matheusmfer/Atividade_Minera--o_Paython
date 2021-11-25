
produtovetorial=list()
produtoescalar = 0
vet_1= list()
n=3
for c in range(1,n+1):
    num=int(input('Numero que deseja inserir '))
    vet_1.append(num)
print(vet_1)

vet_2= list()
n=3
for c in range(1,n+1):
    num=int(input('Nome que deseja inserir '))
    vet_2.append(num)
print(vet_2)

for i in range(3):
    produtoescalar += vet_1[i]*vet_2[i]

produtovetorial.append(vet_1[1]*vet_2[2] - vet_1[2]*vet_2[1])
produtovetorial.append(vet_1[0]*vet_2[2] - vet_1[2]*vet_2[0])
produtovetorial.append(vet_1[0]*vet_2[1] - vet_1[1]*vet_2[0])

print('Produto escalar:',produtoescalar)
print('Produto vetorial:',produtovetorial)


