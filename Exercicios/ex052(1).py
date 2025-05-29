n = int(input('Digite um número para verificar se ele é primo: '))
soma = 0
for i in range(1, n+1):
    if n % i == 0:
        soma += 1
if soma != 2:
    print('Esse número não é primo.')
else:
    print('Esse número é primo!')