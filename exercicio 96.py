def area (a,b) :
    area=a*b
    print(f'A área do terrreno {a} por {b} é de {area} metros quadrados ')


print('-=-'*30)
print('Controle dos terrenos do condomínio')
larg=float(input('Insira a largura do terreno (em metros) : '))
compr=float(input('insira o comprimento do terreno (em metros) : '))
area(larg,compr)
print('O programa acabou')