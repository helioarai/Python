
from datetime import date
def voto(m):
    idade=(date.today().year)-m
    print(f'Voce tem {idade} anos ')
    if idade <16 :
            print('Voce não precisa votar ainda')
    elif idade <18:
        print('Voto opcional')   
    elif idade <=65 :
        print('Voto obrigatório')
    elif idade >65 :
        print ('Voto facultativo')
   
nasc=int(input('Que ano voce nasceu : ?'))
voto(nasc)