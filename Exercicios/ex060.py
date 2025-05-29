mult = num = int(input('Digite o número para calcular seu fatorial: '))
print(f'Calculando {num}! = ', end='')
while num != 1:
    print(num, end=' x ')
    mult *= num -1
    num -= 1
print(f'1 = {mult}')