def maior(*c):
    maior=cont=0
    print(f'Analisando os valores : .... ', end=' : ')
    for i in c :        
        print(f' {i}', end = ' , ')
        if i> maior :
            maior=i
    print (f'O maior valor é o {maior}')
    print()
maior (1,5,3,7,9)
maior (23,56,34,5,7,9,0)
maior (3,4)
maior(3)
maior()