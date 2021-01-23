aluno = dict()
aluno['nome']=str(input('Coloque o nome do aluno : '))
aluno['nota']=float(input('Coloque a média do aluno : '))
print(aluno['nome'])
if aluno['nota']<5:
    aluno['situacao']='reprovado'
elif 5<=aluno['nota']<7:
    aluno['situacao']='recuperação'
elif aluno['nota']>=7 :
    aluno['situacao']='aprovado'
for k,v in aluno.items():
    print(f' {k} é igual a {v}')