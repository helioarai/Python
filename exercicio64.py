num=0
cont=0
soma=0
while num!=999 :
    num=float(input('Coloque o número : '))
    if num!=999:
        cont+=1
        soma+=num
print('A soma dos {} termos é igual a {}'.format(cont,soma))


