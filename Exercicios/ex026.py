frase = str(input('Digite uma frase: ').strip().lower())
print(f'A letra A aparece {frase.count("a")} vezes')
print(f'A letra A aparece primeiramente na posição {frase.find("a")+1}')
print(f'A letra A aparece ultimamente na posição {frase.rfind("a")+1}')