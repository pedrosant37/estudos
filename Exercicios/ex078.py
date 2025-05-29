numeros = list()
maior = menor = pos_maior = pos_menor = 0
for i in range(0,5):
    numeros.append(int(input('Digite um número: ')))
for pos, numero in enumerate(numeros):
    if pos == 0:
        maior = menor = numero
        pos_maior = pos_menor = pos
    elif numero > maior:
        maior = numero
        pos_maior = pos
    elif numero < menor:
        menor = numero
        pos_menor = pos
print(f'O maior número foi {maior} na posição {pos_maior+1}.')
print(f'O menor número foi {menor} na posição {pos_menor+1}.')