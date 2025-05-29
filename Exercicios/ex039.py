idade = int(input('Digite sua idade: '))

if idade < 17:
    print(f'Você ainda vai se alistar, falta(m) {17 - idade} ano(s) para você se alistar.')
elif 45 > idade >= 17 :
    print('Está na hora de se alistar!')
else:
    print(f'Seu prazo para se alistar já passou a {idade - 45} anos!')