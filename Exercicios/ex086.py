matriz = [[], [], []], [[], [], []], [[] ,[] , []]
for lin in range(0,3):
    for col in range(0,3):
        n = str(input(f'Digite um número para colocar na posição ({col}, {lin}): '))
        matriz[lin][col] = n
print('=-'*15)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()