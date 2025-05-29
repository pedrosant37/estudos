from time import sleep

continuar = True
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
while continuar:
    print('''   [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        print(f'A soma de {num1} + {num2} é {num1+num2}')
        print('-'*30)
        sleep(2)
    elif opcao == 2:
        print(f'A multiplicação de {num1} e {num2} é {num1*num2}.')
        print('-'*30)
        sleep(2)
    elif opcao == 3:
        if num1 > num2:
            print(f'O {num1} é maior que o {num2}.')
            print('-'*30)
            sleep(2)
        elif num1 < num2:
            print(f'O {num2} é maior que o {num1}')
            print('-' * 30)
            sleep(2)
        else:
            print('O valor dos números são iguais.')
            print('-' * 30)
            sleep(2)
    elif opcao == 4:
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite outro novo número: '))
        print('-' * 30)
        sleep(2)
    elif opcao == 5:
        continuar = False
    else:
        print('Por favor, digite alguma opção corretamente!')
        print('-' * 30)
        sleep(2)
print('Programa terminado!')