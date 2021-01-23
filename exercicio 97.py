def escreva (msg) :
    print('='* (len(msg)+6))
    print(f'   {msg}')
    print('='*(len(msg)+6))

lista=['Hélio Tiaki Tanaka Arai', 'Fazendo curso de Python',
 'Em dezembro de 2020', 'curso muito bom do Gustavo Guanabara ', 'Show de bola']
for i in lista :
    escreva (i)