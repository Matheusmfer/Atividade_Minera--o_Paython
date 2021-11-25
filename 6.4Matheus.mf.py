
print(' Opção 1 ----------------Adição ')
print(' Opção 2 ----------------Subtração  ')
print(' Opção 3 ----------------Multiplicação  ')
print(' Opção 4 ----------------Divisão  ')
op=int(input('Qual calculo matemático deseja realizar :\n'))
if op ==1:
    num=float(input('Forneça o primeiro numero '))
    num2=float(input('Forneça o segundo numero '))
    ad=num+num2
    print('ADIÇÃO', ad)
elif op==2:
    num=float(input('Forneça o primeiro numero '))
    num2=float(input('Forneça o segundo numero '))
    sub=num-num2
    print('SUBTRAÇÃO', sub)
elif op==3:
    num=float(input('Forneça o primeiro numero '))
    num2=float(input('Forneça o segundo numero '))
    mult=num*num2
    print('MULTIPLICAÇÃO', mult)
elif op==4:
    num=float(input('Forneça o primeiro numero '))
    num2=float(input('Forneça o segundo numero '))
    div=num/num2
    print('MULTIPLICAÇÃO', div)