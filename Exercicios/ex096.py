def area(comprimento, profundidade):
    area = comprimento*profundidade
    print(f'A área do terreno é igual a: {area}m² ')

comprimento = int(input('Digite o comprimento do terreno: '))
profundidade = int(input('Digite a profundidade do terreno: '))
area(comprimento, profundidade)