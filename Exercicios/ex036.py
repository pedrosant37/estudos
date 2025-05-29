valor_casa = float(input('Qual o valor da casa: '))
anos = int(input('Em quantos anos irá pagar a casa: '))
salario = float(input('Qual o valor do seu salário: '))
prestacao = (valor_casa+10/100 * valor_casa*anos)/(anos*12)

print(f'Para pagar uma casa de R${valor_casa+10/100 * valor_casa*anos:.2f} em {anos} anos a prestação será R${prestacao:.2f}')
if prestacao > 30/100 * salario:
    print('Financiamento negado!')
else:
    print('Financiamento concedido!')