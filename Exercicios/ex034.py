salario = float(input('Qual o salário: '))

if salario > 1250:
    print(f'O novo salário agora é: R${salario + 10/100 * salario:.2f}')
else:
    print(f'O novo salário agora é: R${salario + 15 / 100 * salario:.2f}')