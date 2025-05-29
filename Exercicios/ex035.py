lado1 = int(input('Primeiro lado: '))
lado2 = int(input('Segundo lado: '))
lado3 = int(input('Terceiro lado: '))

if  lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')