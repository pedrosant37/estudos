numeros = [[], []]

for i in range(1,8):
    n = int(input(f'Digite o {i}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    elif n % 2 == 1:
        numeros[1].append(n)
print(f'Os números pares são: {sorted(numeros[0])}')
print(f'Os números ímpares são: {sorted(numeros[1])}')