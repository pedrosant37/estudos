from random import randint

print('-'*20)
print('Bem-vindo ao jogo de adivinhação!')
usuario = int(input('Digite um número de 0 a 5: '))
computador = randint(0,5)
if usuario == computador:
    print('Você venceu!')
else:
    print("Você perdeu, tente novamente!")