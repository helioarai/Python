def contador (inicio,final,passo):
    elem=inicio
    if inicio<final :
        while elem<= final :
            print(f'{elem:.0f}', end = ' ')
            elem=elem+passo 
        print()
    if inicio>final :
        while elem>= final :
            print(f'{elem:.0f}', end = ' ')
            elem=elem+passo 
        print()


#Programa Principal
contador (1,10,1)
contador (10,0,-2)
i=float(input('Coloque o valor inicial da sua sequencia'))
f=float(input('Coloque o valor final da sua sequencia '))
s=float(input('Coloque o valor do incremento da sua sequencia'))
contador(i,f,s)