from random import shuffle

alunos = []

alunos.append(input("Digite o primeiro aluno: "))
alunos.append(input("Digite o segundo aluno: "))
alunos.append(input("Digite o terceiro aluno: "))
alunos.append(input("Digite o quarto aluno: "))

shuffle(alunos)
print(f'A ordem de apresentação será {alunos}')