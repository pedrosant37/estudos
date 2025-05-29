def maior(*n):
    lista = [*n]
    maior = 0
    for i in range(0, len(lista)):
        if i == 0 or lista[i] > maior:
            maior = lista[i]
    print(maior)

maior(1,2,3,4,5,6,7,8,9,9,10,8,7,6,5,4,3,2,1)