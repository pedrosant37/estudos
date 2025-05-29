km = float(input("Quantos km voce vai viajar?"))

if km > 200:
    print(f'Vai custar R${km*0.45:.2f}')
else:
    print(f"Vai custar R${km*0.5:.2f}.")