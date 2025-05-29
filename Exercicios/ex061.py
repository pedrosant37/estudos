cont = 0
comeco = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
while cont < 10:
    print(comeco, end=' ')
    comeco += razao
    cont += 1