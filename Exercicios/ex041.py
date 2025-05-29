idade = int(input('Digite sua idade: '))

if idade <= 9:
    print('Categoria Mirim!')
elif 9 < idade <= 14:
    print('Categoria Infantil!')
elif 14 < idade <= 19:
    print('Categoria sênior!')
else:
    print('Categoria Master!')