from random import randint
lista = []

def sorteio (n) :    
    for i in range (0,n) :
        lista.append(randint(1,10))


def somapar(t):
    sompar=0
    for f in t:
        if f%2==0 :
            sompar+= f
    print(f'A soma dos números pares da lista {t} de {len(t)} números é igual a {sompar}')


sorteio (54)
somapar(lista)
lista.clear()
sorteio (12)
somapar(lista)