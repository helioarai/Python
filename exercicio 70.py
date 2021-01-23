
nome=' '
soma=produto1000=preçobar=0
while True :
    x=str(input('Voce deseja continuar com a compra (S/N) :')).strip().upper()[0]
    if x =='N':
        break
    produto = str(input('Nome do produto : '))
    preço=float(input('Preço do produto : '))
    if soma==0:
        preçobar=preço
    if preço<preçobar : 
        nome=produto
    if preço > 1000:
        produto1000+=1
    soma+=preço
print ('O produto mais barato é {}'.format(nome))
print ('A total da compra foi de {} reais '.format(soma))
print ('A quantidade total de itens com preço acima de 1000 reais foram {} itens'.format(produto1000))
        