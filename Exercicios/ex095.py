time = list()
jogador = dict()
while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    jogador['Gols'] = list()
    partidas = int(input('Quantas partidas ele jogou?'))
    jogador['Total'] = 0
    for i in range(1, partidas + 1):
        gols = int(input(f' Quantos gols ele fez na partida {i}?: '))
        jogador['Gols'].append(gols)
        jogador['Total'] += gols
    time.append(jogador.copy())
    cont = str(input('Deseja continuar? [S/N]: '))
    if cont[0] in 'Nn':
        break
print('=-'*20)
print(f'{'cod':<4}{'nome':<15}{'gols'}{'total':>15}')
print('=-'*20)
for pos, jog in enumerate(time):
    print(f'{pos:^4}{jog['Nome']:<15}{jog['Gols']}{jog['Total']:>8}')
print('=-'*20)
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if dados == 999:
        break
    print(f'{' -- '}LEVANTAMENTO DO JOGADOR {time[dados]['Nome']}')
    for part, n in enumerate(time[dados]['Gols']):
        print(f'  => Na partida {part}, fez {n} gols. ')

