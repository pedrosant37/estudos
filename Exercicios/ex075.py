n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tupla = n1, n2, n3, n4

print(f'O valor 9 apareceu: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro 3 apareceu primeiramente na posição: {tupla.index(3)+1}')
else:
    print('Não foi digitado nenhum 3.')
print(f'Os números pares foram : ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
