lista=[]
for i in range(0,5):
    lista.append(int(input(f'Digite um número novo para posição {i} : ')))
print(f'O valor máximo da lista é {(max(lista))} e ele está no posição {(lista.index(max(lista)))}')
print(f'O valor mínimo da lista é {(min(lista))} e ele está no posição {(lista.index(min(lista)))}')
