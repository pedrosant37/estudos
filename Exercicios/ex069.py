print('Bem vindo ao Analisador!')
print('-'*30)
maior_de_idade = homens = 0
mulheres_menor_de_20 = 0
while True:
    idade = int(input('Digite a idade de uma pessoa: '))
    if idade > 18:
        maior_de_idade += 1
    while True:
        sexo = str(input('Digite o sexo dessa pessoa [M/F]: ')).strip().upper()[0]
        if sexo in 'FM':
            break
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_de_20 += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(f'''Foram cadastrados:
{maior_de_idade} pessoas com idade superior a 18.
{homens} homens.
{mulheres_menor_de_20} mulheres com menos de 20 anos.''')