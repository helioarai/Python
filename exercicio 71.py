ced50=ced20=ced10=ced5=ced1=0
valor=int(input('Valor a ser sacado :'))
while True :
    if valor>50 :
        ced50=valor//50        
        valor=valor-ced50*50        
    if valor >20:
        ced20=valor//20        
        valor=valor-ced20*20              
    if valor >10:
        ced10=valor//10
        valor=valor-ced10*10        
    if valor>5 :        
        ced5=valor//5
        valor=valor-ced5*5           
    if valor>=1 :
        ced1=valor
        valor=valor-ced1
        break
print('Total de cédulas de 50 : {} cédulas :'.format (ced50))
print('Total de cédulas de 20 : {} cédulas :'.format (ced20))
print('Total de cédulas de 10 : {} cédulas :'.format (ced10))
print('Total de cédulas de 5 : {} cédulas :'.format (ced5))
print('Total de cédulas de 1 : {} cédulas :'.format (ced1))