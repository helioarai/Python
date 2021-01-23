
soma=cont=media=menor=maior=0
x='s'
while x != 'N':
    num=float(input('Digite um número : '))
    cont+=1
    if cont==1:
        maior=menor=num
    if num>maior:
        maior=num
    if num<menor:
        menor=num 
    soma+=num
    x=input('Deseja continuar [S/N] :').strip().upper()[0]    
media=soma/cont
print('Voce digitou {} números e a média foi {}'.format(cont,media))
print('O maior número é o {} e o menor número é o {}'.format(maior,menor))