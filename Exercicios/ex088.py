from random import randint

lista_jogos = []
temp = []

jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
for j in range(0,jogos):
    for i in range(0,6):
        while True:
            n = randint(1,60)
            if n not in temp:
                temp.append(n)
                break
    lista_jogos.append(temp[:])
    temp.clear()
for pos, lista in enumerate(lista_jogos):
    print(f'Jogo {pos+1}: {lista}')