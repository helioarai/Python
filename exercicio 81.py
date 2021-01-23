lista=[]
r='S'
while True :
    num=int(input('Digite um número inteiro para nossa lista :'))
    lista.append(num)
    r=str(input('Deseja continuar (S/N) : ?')).strip().upper()[0]    
    if r=='N':
        break
lista.sort(reverse=True)
print(f'A lista de números em ordem decrescente é {lista}')
print(f'A quantidade total de números da lista é : {(len(lista))}')
if 5 in lista :
    print('O número 5 está na lista')
else :
    print('O número 5 não está na lista')