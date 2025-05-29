print('=-'*30)
print('Bem vindo ao supermercado Mandacaru, passe seus itens aqui!')
print('=-'*30)
total = mais_de_1000 = preco_mais_barato = 0
nome_mais_barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: R$'))
    if nome_mais_barato == '' or preco < preco_mais_barato:
        nome_mais_barato = nome
        preco_mais_barato = preco
    if preco > 1000:
        mais_de_1000 += 1
    total += preco
    while True:
        continuar = str(input('Quer cadastrar mais algum produto? [S/N]:')).strip().upper()[0]
        print('-'*30)
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(f'''O total da compra foi R${total:.2f}
Tiveram {mais_de_1000} produtos com mais de R$1000,00
O produto mais barato foi {nome_mais_barato} com o preco de R${preco_mais_barato:.2f}''')
