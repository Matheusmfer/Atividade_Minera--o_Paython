a_0=0
a_1=1
cont=3
n=int(input('Quantidade de termos: '))
print('{} . {}'.format(a_0, a_1), end='')

while cont <= n:
    a_n = a_0 + a_1
    a_0 = a_1
    a_1= a_n
    cont += 1
    print(' . {}'.format(a_n), end='')