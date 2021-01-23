def leiaint(msg):
    ok=False
    valor=0
    while True :
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok = True
        else :
            print('Número inválido , digite novamente : ')
        if ok :
            break
    return valor

#Programa principal
n=leiaint('Digite um número')
print(f'Voce acabou de digitar um número {n}')