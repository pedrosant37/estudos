times = ('Palmeiras','Flamengo','Fluminense','Bragantino','Ceará','Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Juventude', 'São Paulo', 'Mirassol', 'Internacional', 'Bahia', 'Fortaleza', 'Botafogo', 'Vitória', 'Atlético - MG', 'Santos', 'Grêmio', 'Recife')
print(f'Os 5 primeiros colocados são: ')
print('='*30)
for i in range(1,6):
    print(f'{i}°', times[i])
print('=' * 30)
print(f'Os últimos colocados são: ')
print('='*30)
for i in range(16, 20):
    print(f'{i+1}°', times[i])
print('='*30)
print(f'Os times em ordem alfabética são: ')
print('='*30)
for time in sorted(times):
    print(f'{time}')
print('='*30)
print(f'O Fortaleza está na posição {times.index('Fortaleza')+1}°')
