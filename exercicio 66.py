cont=soma=num=0
while num!=999 :
    num=int(input('Digite o número [999 para finalizar o programa]'))
    if num==999:
        break        
    soma+=num
    cont+=1
print(f'O número total de números é {cont} e a soma é igual a {soma}')