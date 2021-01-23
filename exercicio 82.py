lista=[]
listapar=[]
listaimpar=[]
r='S'
while True :
    lista.append (int(input('Digite um número inteiro para nossa lista :')))
    r=str(input('Deseja continuar (S/N) : ?')).strip().upper()[0]     
    if r=='N':
        break
print(lista,listapar,listaimpar)  
for v in lista :
    print (v)
    if v%2==0:
        listapar.append(v)        
    elif v%2==1 :
        listaimpar.append(v)
print(f'A lista total é {lista}')
print(f'A lista de números pares é {listapar}')
print(f'A lista de números ímpares é {listaimpar}')

 