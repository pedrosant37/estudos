pessoa = dict()

pessoa['Nome'] = str(input('Nome:')).strip()
pessoa['Idade'] = 2025 - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho [0 se não tem]: '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratatação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Ano de aposentadoria'] = pessoa['ano_contrat'] + 35
print('=-'*15)
for k, v in pessoa.items():
    print(f'{k} é {v}')
