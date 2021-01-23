
from random import randint
n=(randint(1,10),randint(1,10), randint(1,10), randint(1,10),randint(1,10)  )
print('Eu sorteei os valores :')
for i in n:
    print(f'{i}', end=' ')
print(f'\nO maior valor sorteado foi {max (n)}')
print(f'O menor valor sorteado foi {min (n)}')