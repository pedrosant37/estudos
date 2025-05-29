def leiaint():
    try:
        inteiro = int(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar os dados')
        inteiro = 0
        real = 0
    except (ValueError, TypeError):
        inteiro = int(input('Erro, digite um número inteiro.'))
    try:
        real = float(input('Digite um número real: '))
    except (ValueError, TypeError):
        real = float(input('Erro, digite um número inteiro: '))
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar os dados')
        real = 0
    finally:
        print()


leiaint()