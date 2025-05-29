quant = menor = maior = soma = 0
continuar = 's'

while continuar in 'Ss':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if quant == 0 or num < menor:
        menor = num
    soma += num
    quant += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip()[0]
print(f'Você digitou {quant} número(s) e a média foi {soma/quant}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
