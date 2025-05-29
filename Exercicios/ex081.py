numeros = list()

while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{len(numeros)} números foram digitados.')
print(f'A lista ordenada em ordem descrescente: {numeros.sort(reverse=True)}')
if 5 in numeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
