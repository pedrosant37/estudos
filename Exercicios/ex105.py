def notas(*n, sit=False):
    """

    :param n: recebe as notas dos alunos para manipulação
    :param sit: se colocado como verdadeiro, retorna a situação do aluno
    :return: retorna um dicionario com métricas do aluno
    """
    geral = dict()
    soma = 0
    geral['total'] = len(n)
    for i in range(0, len(n)):
        soma += n[i]
        if i == 0:
            geral['maior'] = n[i]
            geral['menor'] = n[i]
        elif n[i] > geral['maior']:
            geral['maior'] = n[i]
        elif n[i] < geral['menor']:
            geral['menor'] = n[i]
    geral['media'] = soma / len(n)
    if sit:
        if geral['media'] < 6:
            geral['situação'] = 'RUIM'
        elif geral['media'] >= 8:
            geral['situação'] = 'ÓTIMA'
        else:
            geral['situação'] = 'BOA'
    return geral


print(notas(7,8,9, sit=True))