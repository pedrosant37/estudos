from ex107 import moedas

p = float(input('Digite o valor: R$'))
print(f'A metade de {p} é R${moedas.metade(p):.2f}')
print(f'O dobro de {p} é R${moedas.dobro(p):.2f}')
print(f'Aumentando 10%, temos R${moedas.aumentar(p, 10):.2f}')
print(f'Diminuindo 13%, temos R${moedas.diminuir(p, 13):.2f}')