maioridade = 0
minoridade = 0
for i in range(0,7):
    ano = int(input('Digite o ano de nascimento de uma pessoa:'))
    if 2025 - ano >= 18:
        maioridade += 1
    else:
        minoridade += 1
print(f'Maiores de idade: {maioridade}')
print(f'Menores de idade: {minoridade}')
