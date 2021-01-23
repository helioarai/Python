dado=list()
turma=list()
for i in range (0,3):
    dado.append(str(input('Coloque o nome :')))
    dado.append(int(input('Coloque a idade :')))
    turma.append(dado[:])
    dado.clear()
print(turma)

    