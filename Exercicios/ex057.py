sexo = 'g'
while sexo not in 'mf':
    sexo = input('Digite seu sexo [M] ou [F]: ')
    if sexo not in 'mf':
        print('Por favor, insira a informação corretamente.')
print('Obrigado!')
