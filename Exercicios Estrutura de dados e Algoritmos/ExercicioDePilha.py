redoStack = []
backStack = []
site = ''
while True:
    if site == '':
        print('Você ainda não está em nenhum site!')
    else:
        print(f'Você está no site {site}')
    opcao = int(input('O que você quer fazer?:\n'
                      '1) Ir para um site\n'
                      '2) Voltar\n'
                      '3) Ir para frente\n'
                      'Opção: '))
    if opcao == 1:
        if site != '':
            backStack.append(site)
        site = input('Digite um site: ')

    elif opcao == 2:
        if len(backStack) == 0:
            print('Você não foi em nenhum site anteriormente.')
        else:
            redoStack.append(site)
            site = backStack[-1]
            backStack.pop()
    else:
        if len(redoStack) == 0:
            print('Você não foi em nenhum site posterior a esse.')
        else:
            backStack.append(site)
            site = redoStack[-1]
            redoStack.pop()
