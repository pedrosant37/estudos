nome = input('Digite seu nome: ')

print(f'Seu nome em letras maiusculas fica: {nome.upper()}')
print(f'seu nome em letras minusculas fica: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(' ', ''))} letras')
print(f'Seu primeiro nome: {nome.split()[0]} tem {len(nome.split()[0])} letras')