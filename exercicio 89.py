lista=list()
while True :
    nome=str(input('Coloque o nome do estudante :'))
    nota1=(float(input('Coloque a primeira nota :')))
    nota2=(float(input('Coloque a segunda nota :')))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    c=str(input('Deseja continuar (S/N)')).strip().upper()[0]
    if c=='N':
        break
print(f'{"N.o":<4}{"Nome" :<20} {"Média":>10}')
for i,n in enumerate(lista):
    print(f'{i:<4}{n[0]:<20}{n[2]:>10}')
while True :
    opc=int(input('Deseja verificar as notas do aluno ? (999 para finalizar):'))
    if opc== 999 :
        print('Finalizando ')
        break
    if opc<len(lista):
        print(f'{opc:<4}{lista[opc][0]:<20}{lista[opc][1]}')



