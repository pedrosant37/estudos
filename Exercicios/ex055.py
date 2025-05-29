maior = 0
menor = 0

for i in range(0,5):
    peso = float(input('Digite um peso: '))
    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'Maior peso: {maior} kgs')
print(f'Menor peso: {menor} kgs')