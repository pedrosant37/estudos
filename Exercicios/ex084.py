pessoas = list()
dados = list()
maior_peso = 0
menor_peso = 0
while True:
     dados.append(str(input('Digite o nome da pessoa: ')))
     peso = float(input('Digite o peso da pessoa: '))
     if maior_peso == 0:
         maior_peso = peso
         menor_peso = peso
     elif maior_peso < peso:
         maior_peso = peso
     elif menor_peso > peso:
         menor_peso = peso
     dados.append(peso)
     pessoas.append(dados[:])
     del dados[:]
     continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
     if continuar == 'N':
         break
print(f'{len(pessoas)} pessoas foram adicionadas.')
print(f'O maior peso foi {maior_peso}kg de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end='')
print(end='\n')
print(f'O menor peso foi {menor_peso}kg de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end='')