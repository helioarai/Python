from Util import aumentar,diminuir,metade,dobro

# Programa Principal
preco=float(input('Digite o valor do produto : '))
print(f'O preço com aumento de {10} % é de R$ {aumentar(10,preco):.2f}')
print(f'O preço com desconto de {10} % é de R$ {diminuir(10,preco):.2f}')
print(f'O dobro do preço de {preco} % é de R$ {dobro(preco):.2f}')
print(f'A metade do preço de {preco} é de R$ {metade(preco):.2f} ')