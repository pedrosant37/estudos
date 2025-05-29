ano = int(input('Digite um ano:'))
if ano % 100 == 0 or ano % 4 != 0:
    print('Esse ano não é bissexto.')
else:
    print('Esse ano é bissexto!')