cont = soma = 0
while True:
     num = int(input('Digite um número [999 para parar]: '))
     if num == 999:
         break
     cont += 1
     soma += num
print(f'A quantidade de números digitados foram: {cont}, e a soma entre eles: {soma}.')
