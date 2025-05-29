def dobro(n):
    return f'R${n*2:.2f}'

def metade(n):
    return f'R${n/2:.2f}'

def aumentar(n, porcentagem):
    return f'R${n+porcentagem/100*n:.2f}'

def diminuir(n, porcentagem):
    return f'R${n-porcentagem/100*n:.2f}'