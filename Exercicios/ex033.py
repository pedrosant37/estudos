lista = []

n1 = lista.append(int(input('Digite o primeiro número: ')))
n2 = lista.append(int(input('Digite o segundo número: ')))
n3 = lista.append(int(input('Digite o terceiro número: ')))

lista.sort()
print(f'O maior número é {lista[2]}, e o menor é {lista[0]}')


