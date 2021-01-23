def leiaint(msg):
    while True :
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('Número inválido. Digite novamente um número inteiro válido')
            continue
        else :
            return n
    

def leiareal(msg):
    while True :
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print('Número inválido. Digite novamente um número inteiro real')
            continue
        else :
            return n


#Programa principal
num=leiaint('Digite um número inteiro : ')
print(f'Voce acabou de digitar um número {num}')

numr=leiareal('Digite um número real : ')
print(f'Voce acabou de digitar um número {numr:4.2f}')