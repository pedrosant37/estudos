print('-'*30)
print('Bem vindo ao caixa eletrônico!')
print('-'*30)
valor = int(input('Digite o valor a ser sacado: '))
cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0
while True:
    if valor >= 50:
        valor -= 50
        cedula_50 += 1
    elif valor >= 20:
        valor -= 20
        cedula_20 += 1
    elif valor >= 10:
        valor -= 10
        cedula_10 += 1
    elif valor >= 1:
        valor -= 1
        cedula_1 += 1
    else:
        break
if cedula_50 > 0:
    print(f'Total de {cedula_50} cédulas de R$50')
if cedula_20 > 0:
    print(f'Total de {cedula_20} cédulas de R$20')
if cedula_10 > 0:
    print(f'Total de {cedula_10} cédulas de R$10')
if cedula_1 > 0:
    print(f'Total de {cedula_1} cédulas de R$1')



