from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
maior = menor = 0
tupla = (n1, n2, n3, n4, n5)
for i in range(0,5):
    if i == 0:
        maior = tupla[i]
        menor = tupla[i]
    elif tupla[i] > maior:
        maior = tupla[i]
    elif tupla[i] < menor:
        menor = tupla[i]
print(f'O maior valor da tupla é {maior}')
print(f'O menor valor da tupla é {menor}')