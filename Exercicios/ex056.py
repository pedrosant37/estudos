soma = 0
idade_mais_velho = 0
nome_mais_velho = ''
mulheres_menor_de_20 = 0
for i in range(1,5):
    nome = input(f'Digite o nome da {i} pessoa: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = input(f'Digite o sexo de {nome} [M] ou [F]: ').lower().strip()
    soma += idade
    if i == 1 and sexo =='m':
        nome_mais_velho = nome
        idade_mais_velho = idade
    elif sexo == 'm' and idade > idade_mais_velho:
        nome_mais_velho = nome
        idade_mais_velho = idade
    elif sexo == 'f' and idade < 20:
        mulheres_menor_de_20 += 1
print(f'A média das idades foi {soma/4}')
print(f'O nome do mais velho é: {nome_mais_velho}')
print(f'A quantidade de mulheres menos de 20 anos é: {mulheres_menor_de_20}')

