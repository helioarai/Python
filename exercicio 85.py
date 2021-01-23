dados=[[],[]]
for i in range (1,8) :
    num = (int(input('Coloque o número :')))
    if num%2==0 :
        dados[0].append(num)
    else :
        dados[1].append(num)
dados[0].sort()
dados[1].sort()
print(f'Os números pares são {dados[0]}',f'Os núemros ímpares são {dados[1]}')  

