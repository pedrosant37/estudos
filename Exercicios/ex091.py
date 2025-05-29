from random import randint
from time import sleep
from operator import itemgetter

cont = 1
jogadores = {'jogador1': randint(1,6),'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4':randint(1,6)}
for k, v in jogadores.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in sorted(jogadores.items(), reverse=True):
    print(f'{cont}° Lugar: {k} com {v}')
    cont += 1
print(ranking)