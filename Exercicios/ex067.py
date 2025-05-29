while True:
    n = int(input('Digite um número para ver sua tabuada [Tecle um número negativo para sair]: '))
    if n < 0:
        break
    print('-'*30)
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    print('-'*30)
print('Programa terminado.')