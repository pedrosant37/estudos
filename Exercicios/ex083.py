expr = str(input('Digite sua expressão numérica: '))
pilha = list()
for sim in expr:
    if sim == '(':
        pilha.append(sim)
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(sim)
            break
if len(pilha) > 0:
    print('Sua expressão não é válida')
else:
    print('Sua expressão é válida.')
