' Importação da biblioteca math'
import math
import numpy
'Definição e leitura  da variavel grau '
grau= float(input('Forneça o valor em graus :'))
' Definição e conversão da variavel grau em radiano rad'
rad = numpy.deg2rad(grau)
'Impressão da variavel rad '
print('Convertido para :', rad)
'Definição das propriedades trigonometricas '
coss= math.cos(grau)
senn=math.sin(grau)
tang=math.tan(grau)
'Impressão das propriedades trigonometricas '
print('Cosseno:', coss)
print('Seno:', senn)
print('Tangente:', tang)