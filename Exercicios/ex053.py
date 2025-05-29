from math import ceil

frase = input('Digite uma frase: ').lower().replace(' ', '')
lidas1 = ''
lidas2 = ''
for i in range(0, int(ceil(len(frase)/2))):
    lidas1 += frase[i]
for i in range(len(frase)-1, int(len(frase)/2-1), -1):
    lidas2 += frase[i]
if lidas1 == lidas2:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo')