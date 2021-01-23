cadastro=[]
pessoa={}
soma=media=0
pessoa['sexo']='T'
while True :
    pessoa.clear()
    pessoa['nome']=str(input('Coloque o nome da pessoa : '))
    while True :
        pessoa['sexo']=str(input('Coloque o sexo (M/F) : ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, digite somente (M/F)')
    pessoa['idade']=int(input('Coloque a idade da pessoa : '))
    soma+=pessoa['idade']
    cadastro.append(pessoa.copy())
    if len(cadastro)==1 :
        media=soma
    else :
        media=soma/(len(cadastro))    
    while True :
        opc=str(input('Voce quer continuar (S/N) :')).strip().upper()[0]
        if opc in 'SN':
            break
        print('Erro , digite somente (S/N)')
    if opc =='N':
        break
print(f'O numero total de pessoas cadastradas é {len(cadastro)}')

print(f'A média da idade das pessoas é de {media} anos')
print(' As mulheres da lista são : ')
for p in cadastro :
    if p['sexo']=='F' :
        print (p['nome'], end =' ')
    print( )
print (' As pessoas da  lista que tem idade superior à média são : ')
for t in cadastro :
    if t['idade']>=media :
        print(t['nome'], end =' ')
    