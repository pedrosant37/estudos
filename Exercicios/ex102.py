def fatorial(n, show=False):
    for i in range(n, 1, -1):
        n *= i-1
    if show:
        print(n)
    else:
        return n


print(fatorial(8))