velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print(f"Você foi multado, e deverá pagar: R${(velocidade - 80)*7},00")
else:
    print('Continue sua viagem com segurança!')