
def fatorial (num, show=False):
    """ O fatorial de um número é calculado multiplicando o número
    pelo seu número menor sucessivamente até o número 1 """
    fato=1
    for i in range (num,0,-1):
        fato*=i
    if show :
        print('A sequencia do  fatorial é :', end= ' ')
        for i in range (num,0,-1):
            if i ==1 :
                print(f' {i} = {fato}')
            else : 
                print(f' {i} x', end=' ')
    return fato


numero=int(input('Coloque o número que deseja calcular o fatorial'))
result = fatorial(numero,show=True)
print(f'O numero {numero} ! é igual a {result}')
help(fatorial)