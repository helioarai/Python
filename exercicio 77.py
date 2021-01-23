palavras=('aprender', 'correr', 'estudar',
'andar','exercitar', 'apartamento','zoologico',
'andarilho', 'colegio', 'combinar')
for i in palavras :
    print(f'\nAs vogais da palavra {i.upper()} são :',end= ' ')
    for letra in i :
        if letra.lower()in 'aeiou' :
            print(letra,end=' ')
    