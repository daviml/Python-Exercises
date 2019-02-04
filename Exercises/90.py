aluno = {}

aluno['nome'] = str(input('digite o nome do aluno: '))
aluno['media'] = int(input(f'digite a media de {aluno["nome"]}: '))
if (aluno['media']) >= 7:
    aluno['situacao'] = 'aprovado'
for k,v in aluno.items():
    print(k,v)
    print()
