
num=0
while True:
    num=int(input('Voce quer ver a tabuada de qual número inteiro (número negativo finaliza)? :'))
    if num< 0 :
        break
    for i in range (1,11) :        
        print (' {} * {} = {}'. format (num,i,num*i))
print('Acabou')