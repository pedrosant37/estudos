jogador = dict()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
jogador['Gols'] = list()
partidas = int(input('Quantas partidas ele jogou?'))
jogador['Total'] = 0
for i in range(1,partidas+1):
    gols = int(input(f'Quantos gols ele fez na partida {i}?: '))
    jogador['gols'].append(gols)
    jogador['Total'] += gols
print('=-'*15)
print(jogador)
print('=-'*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*15)
print(f'O jogador {jogador['Nome']} jogou {partidas} partidas.')
for p, g in enumerate(jogador['Gols']):
    print(f'    => Na partida {p}, fez {g} gols. ')
print(f'Foi um total de {jogador['Total']} gols.')
