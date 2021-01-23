dado=list()
turma=list()
mai=men=0
while True :
    dado.append(str(input('Coloque o nome :')))
    dado.append(int(input('Coloque o peso :')))
    if len(turma)==0 :
        mai=men=dado[1]
    else :
        if mai<dado[1]:
            mai=dado[1]
        if men>dado[1]:
            men=dado[1]
    turma.append(dado[:])
    dado.clear()
    c=str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if c =='N' :
        break
print(f'O número de pessoas cadastradas é {len(turma)} ')
print (turma)
print(f'O maior peso de {mai} Kg foi do : ', end=' ')
for i in turma :
    if i[1]==mai :
        print (f'[{i[0]}]',end=' ')        
print(f'\nO menor peso de {men} Kg foi do : ', end=' ')
for i in turma:
    if i[1]==men:
        print(f'[{i[0]}]', end=' ')
    