
tot=(int(input('Digite um número : ')),
int(input('Digite mais um número : ')),
int(input('Digite mais um número : ')),
int(input('Digite o último número : ')))
print (f'Voce digitou os números {tot}:')
print(f'O número 9 apareceu {(tot.count(9))} vezes')
print(f'O valor 3 apareceu na {(tot.index(3))+1} posição ')
print ('Os números pares da sequencia são : ')
for n in tot :
    if n%2==0 :
        print (n, end=' ')