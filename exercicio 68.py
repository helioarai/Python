from random import randint
print('Jogo de par ou impar :')
cont=0
while True :
    dedos=int(input('Quantos dedos ? :'))
    comput=randint(1,10)
    soma=dedos+comput
    esco=' '
    while esco not in 'PI':
        esco=input('Par ou impar : [P/I]').strip().upper()[0]
    print(f'Computador: {comput}, voce :{dedos}, total: {soma}')
    if soma%2 ==0 :
        if esco=='P':
            print ('Voce venceu ')
            cont+=1
        else :
            print ('Voce perdeu')
            break
    elif soma%2 ==1 :
        if esco=='I' :
            print('Voce venceu ')
            cont+=1
        else :
            print('Voce perdeu')
            break
    print('Vamos jogar novamente !!!  ')
print(f'Game Over , voce venceu {cont} vezes, o computador venceu 1 vez')
