quant = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    quant += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {quant} números e a soma entre eles foi: {soma}.')

