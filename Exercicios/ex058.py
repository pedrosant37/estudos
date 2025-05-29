from random import randint
certo = False
tentativas = 0
numero_pc = randint(0,11)
print('Eu escolhi um número de 0 a 10, será que você consegue acertar?')
while not certo:
    numero_user = int(input('Digite um número de 1 a 10: '))
    if numero_user < 0 or numero_user > 10:
        print('Tente novamente!')
    else:
        tentativas += 1
        if numero_user == numero_pc:
            certo = True
        elif numero_user > numero_pc:
            print('Menos... tente mais uma vez.')
        elif numero_user < numero_pc:
            print('Mais... tente mais uma vez')
print(f'Você ganhou em {tentativas} tentativas!')