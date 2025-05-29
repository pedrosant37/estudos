from random import randint

print('-='*15)
print('Vamos jogar Par Ou Ímpar')
sequencia = 0

while True:
    print('-=' * 15)
    pc = randint(0,10)
    usuario = int(input('Digite um número: '))
    opcao = str(input('Par ou Ímpar [P/I]: ')).strip().lower()[0]
    soma = usuario + pc
    print('-' * 30)
    print(f'Você jogou {usuario} e o computador {pc}. Total de {soma}', 'DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    print('-'*30)
    if opcao == 'p' and soma % 2 == 0 or opcao == 'i' and soma % 2 == 1:
        print('Você venceu!')
        print('Vamos jogar novamente...')
        sequencia += 1
    else:
        print('Você perdeu')
        break
print('=-'*15)
print(f'Game Over, Você venceu {sequencia} vezes.')

    
