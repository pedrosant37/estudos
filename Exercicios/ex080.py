numeros = list()
cont = 0
for i in range(0,5):
    num = int(input('Digite um valor: '))
    if i == 0:
        numeros.append(num)
    else:
        while True:
            if num <= numeros[cont]:
                numeros.insert(cont, num)
                cont = 0
                break
            if num > numeros[cont]:
                numeros.append(num)
                cont = 0
                break
            else:
                cont += 1
print(numeros)