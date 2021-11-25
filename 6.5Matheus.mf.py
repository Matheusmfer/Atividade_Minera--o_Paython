n=int(input('Numero que deseja fatorar '))
for c in range (1, n+1):
    if n%c==0:
        print ('{}'.format(c))
