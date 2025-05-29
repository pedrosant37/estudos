dias = int(input("Quantos dias o carro foi alugado?: "))
km = float(input("Quantos km rodados?: "))

print(f"O preço a pagar é R${dias*60+km*0.15:.2f}.")
