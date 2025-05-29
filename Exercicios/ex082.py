numeros = list()
pares = list()
impares = list()

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista de números adicionados foi: {numeros.sort()}')
print(f'A lista de números pares foi: {pares.sort()}')
print(f'A lista de números impares foi: {impares.sort()}')

