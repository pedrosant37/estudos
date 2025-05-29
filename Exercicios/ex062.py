cont = 10
comeco = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
while cont > 0:
    print(comeco, end=' ')
    comeco += razao
    cont -= 1
    if cont == 0:
        cont = int(input('Qantos termos você quer mostrar a mais? '))