
lista=('Lápis',.75,
'Borracha', 2.00,
'Caderno', 15.90,
'Estojo',25,
'Transferidor',4.2,
'Compasso',9.9,
'Mochila',120.32,
'Canetas',22.3,
'Livros',34.98)
print('*'*40)
print(f'{"Listagem de preços":-^40}')
print('*'*40)
for i in range (0, len(lista)):
    if i%2==0 :
        print(f'{lista[i]:.<30}',end='')
    else :
        print(f'R$  {lista[i]:>7.2f}')
print('*'*40)