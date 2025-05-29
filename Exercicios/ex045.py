from random import choice

opcoes = ['pedra', 'papel', 'tesoura']

print('''Suas opções
[0] pedra
[1] papel
[2] tesoura''')

jogada_player = int(input('Qual a sua jogada: '))
jogada_comp = choice(opcoes)

print(f'O jogador jogou {opcoes[jogada_player]} e o computador jogou {jogada_comp}')

if jogada_comp == opcoes[jogada_player]:
    print('Empate')
elif jogada_comp == 'pedra' and opcoes[jogada_player] == 'papel':
    print('Você ganhou!')
elif jogada_comp == 'papel' and opcoes[jogada_player] == 'tesoura':
    print('Você ganhou!')
elif jogada_comp == 'tesoura' and opcoes[jogada_player] == 'pedra':
    print('Você ganhou!')
else:
    print('Você perdeu!')

