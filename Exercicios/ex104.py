def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        print('Erro, digite um número inteiro válido.')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
