from random import randint


def sortear_somar(list):
    pares = 0
    for i in list:
        if i % 2 == 0:
            pares += i
    print(pares)


sortear_somar([randint(0,10), randint(0,10), randint(0,10), randint(1,10), randint(0,10)])