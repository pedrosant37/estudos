preco = float(input('Qual o preço das compras?: R$'))
print("""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - 10/100 * preco:.2f}')
elif opcao == 2:
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - 5/100 * preco:.2f}')
elif opcao == 3:
    print(f'Sua compra de R${preco:.2f} não terá alteração no valor')
else:
    parcelas = int(input('Em quantas parcelas?: '))
    print(f'Sua compra será parcelada em {parcelas}X de R${(preco + 20/100 * preco)/parcelas:.2f}')
    print(f'Sua compra de R${preco:.2f} no final custará R${preco + 20/100 * preco:.2f}')