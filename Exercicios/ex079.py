numeros = list()
while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        print('Esse número já foi digitado, tente outro valor.')
    else:
        numeros.append(num)
        continuar = str(input('Quer continuar? [S/N]: '))
        if continuar[0] not in 'SsNn':
            while continuar[0] not in 'SsNn':
                continuar = str(input('Digite S ou N:'))
        if continuar[0] in 'Nn':
            break
print(f'A ordem crescente dos valores é: {numeros.sort()}')
