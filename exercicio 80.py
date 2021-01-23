lista=[]
for i in range (0,5):
    novo=float(input('Digite um valor : '))
    if i==0 or novo>lista[-1]:
        lista.append(novo)
    else :
        pos=0 
        while pos<len(lista):
            if novo <=lista[pos]:
                lista.insert(pos,novo)
                break
            pos+=1
print(f'A lista de números em ordem crescente é {lista}')
