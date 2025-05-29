def ficha_jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')
nome = str(input('Digite o nome do jogador: '))
gols = int(input('Digite a quantidade de gols que ele fez no campeonato: '))
ficha_jogador(nome, gols)