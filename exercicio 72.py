
cont=('zero','um', 'dois','tres', 'quatro','cinco',
'seis','sete','oito','nove','dez','onze','doze','treze',
'catorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True :
    while True :
        num=int(input('Digite um número entre 0 e 20 :'))
        if   0<= num <=20 :
            break
        print('Número inválido. Tente novemente', end= ' ')
    print(f'O número escolhido pelo cliente é {cont[num]}')
    c=str(input('Voce quer continuar (S/N)')).strip().upper()[0]
    if c == 'N':
        break
print('O programa acabou ...')