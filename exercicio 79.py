lista=[]
esc='S'
while esc != 'N':
    novo=float(input('Digite um valor : '))
    if novo not in lista :
        print ('Numero adicionado com sucesso')
        lista.append(novo)
    else :
        print ('Número já adicionado :')
    esc=str(input('Deseja continuar (S/N) ? :')).strip().upper()[0]
lista.sort()
print(f'A lista de números em ordem crescente é {lista}')
