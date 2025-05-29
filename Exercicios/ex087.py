matriz = [[], [], []],[[], [], []], [[], [], []]
pares = maior = 0
somacoluna3 = 0
for lin in range(0,3):
    for col in range(0,3):
        n = int(input(f'Digite um número para colocar na posição ({col}, {lin}): '))
        matriz[lin][col] = n
        if n % 2 == 0:
            pares += n

print('=-'*15)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
        if col == 2:
            somacoluna3 += matriz[lin][col]
        if lin == 1 and col == 0:
            maior = matriz[lin][col]
        elif lin == 1:
            if matriz[lin][col] > maior:
                maior = matriz[lin][col]

    print()
print('=-'*15)
print(f'A soma dos números pares da matriz é: {pares}')
print(f'A soma dos valores da terceira coluna é: {somacoluna3}')
print(f'O maior número da segunda linha é: {maior}')