tupla = 'quero', 'ser', 'o', 'melhor', 'programador', 'do', 'mundo'

for palavra in tupla:
    print(end='\n')
    print(f'Na palavra {palavra} temos: ', end='')
    for i in range(0,len(palavra)):
        if palavra[i] in 'aeiou':
            print(palavra[i], end=' ')
