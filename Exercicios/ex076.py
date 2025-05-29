tabela = ('GTA VI', 600, 'Hollow Knight: Silksong', 200, 'Call of Duty: 2', 50)

for i in range(0,len(tabela),2):
    print(f'{tabela[i]:.<30}', f'R${tabela[i+1]:>8.2f}')