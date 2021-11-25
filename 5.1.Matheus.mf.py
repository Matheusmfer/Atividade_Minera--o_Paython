'Definição e leitura da variavel n '
n=float (input('Forneça o valor em reais:'))
' Para saber o numero mínimo de notas necessárias devemos adquirir o rwsutado divisão de n pelo valor da nota '
div_1= n/100
div_2= n/50
div_3= n/10
div_4=n/1
print('Para nota de 100:',div_1)
print('Para nota de 50:',div_2)
print('Para nota de 10:',div_3)
print('Para nota de 1:',div_4)