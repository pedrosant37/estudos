comeco = int(input('Digite o comeco da PA: '))
razao = int(input('Digite a razao da PA: '))
print('Os dez primeiros termos dessa PA são:', end='')
for i in range(0,10):
    print(comeco, end=' ')
    comeco+=razao