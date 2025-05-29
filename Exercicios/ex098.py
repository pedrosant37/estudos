def contar():
    from time import sleep
    print('=-'*20)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1,11):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')
    print('=-' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, 0, -2):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')
    print('=-'*20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('INICIO: '))
    fim = int(input('FIM: '))
    passo = int(input('PASSO: '))
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = +passo
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo > 0:
        passo = -passo
        fim -= 2
    for i in range(inicio, fim+1, passo):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')




contar()

