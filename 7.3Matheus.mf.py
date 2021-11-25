frase = str(input('Escreva uma mensagem: '))
cod = ''
nome = False

for i in frase:
    if i.isupper():
        nome = True
        cod += '∗'
        continue
    if nome:
        if i.isalpha():
            cod += '∗'
            continue
        else:
            cod += i
            nome = False
    else:
        cod+= i
print([cod])