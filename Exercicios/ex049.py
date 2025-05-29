n = int(input("Digite um número para ver sua tabuada: "))

print("-"*20)
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
print("-"*20)