dados=[[],[],[]]
somapar=somater=maior=0
for i in range (0,3) :
    for n in range (0,3):
        num = (int(input(f'Coloque o número para posição({i} : {n})  :')))
        dados[i].append(num)
        if num%2==0:
            somapar+=num
        if i==1:
            if num>maior :
                maior=num
        if n==2:
            somater+=num
        n+=1
for i in dados:
    for n in range (0,3):
        print(f'[{i[n]:^5}]', end=' ')
        n+=1
    print( )
print(f'A soma dos números pares é igual a {somapar}')
print(f'A soma dos números da terceira coluna é igual a {somater}')
print(f'O maior número da segunda coluna é {maior}')