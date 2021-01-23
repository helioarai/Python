dados=[[],[],[]]
for i in range (0,3) :
    for n in range (0,3):
        num = (int(input(f'Coloque o número para posição({i} : {n})  :')))
        dados[i].append(num)
        n+=1
for i in dados:
    for n in range (0,3):
        print(f'[{i[n]:^5}]', end=' ')
        n+=1
    print( )