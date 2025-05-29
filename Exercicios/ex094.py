pessoas = list()
pessoa = dict()
mulheres = list()
acima_da_media = list()
total = media = 0
soma_idades = 0

while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    idade = int(input('Idade: '))
    pessoa['idade'] = idade
    soma_idades += idade
    pessoas.append(pessoa.copy())
    total += 1
    cont = str(input('Deseja continuar? [S/N]: '))
    print(pessoas)
    if cont[0] in 'Nn':
        break
media = soma_idades / len(pessoas)
for i in pessoas:
    if i['sexo'][0] in 'Ff':
        mulheres.append(i)
    if i['idade'] > media:
        acima_da_media.append(i)
print(f'O total de pessoas cadastradas foi: {total}')
print(f'A média de idade das pessoas foi: {media}')
print(f'A lista de mulheres cadastradas: {mulheres}')
print(f'A lista de pessoas com idade acima da média: {acima_da_media}')

