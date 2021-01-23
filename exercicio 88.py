from random import randint
aposta=[]
dados=[]
from time import sleep
jogos=int(input('Quantos jogos voce vai querer gerar ? :'))
for i in range (0,jogos) :
    for n in range (1,6) :
        if n==1 :
           dados.append(randint(1,60))
        while True :
           novo=(randint(1,60))
           if dados.count(novo)==0 :
               dados.append(novo)    
               break   
    dados.sort()   
    aposta.append(dados[:])
    dados.clear()
for i,l in enumerate (aposta):
    print(f' jogo {i+1} : {l}')
    sleep(0.5)
