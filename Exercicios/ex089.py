alunos = []
temp = []
while True:
    temp.append(input('Digite o nome do aluno: '))
    temp.append(float(input('Digite a primeira nota do aluno: ')))
    temp.append(float(input('Digite a segunda nota do aluno: ')))
    alunos.append(temp[:])
    temp.clear()
    cont = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if cont == 'N':
        break
print('=-'*30)
print(f'{'No.':<4}{'NOME':<15}{'MÉDIA'}')
print('-'*30)
for pos, dados in enumerate(alunos):
    print(f'{pos:<4}{dados[0]:<15}{(dados[1] + dados[2])/2}')
print('-'*30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if aluno == 999:
        break
    print(f'Notas de {alunos[aluno][0]}: {alunos[aluno][1:]}')