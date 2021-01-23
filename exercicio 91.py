from random import randint
from operator import itemgetter

turma={'jogador 1': randint(1,6) , 
'jogador 2' : randint(1,6) , 
'jogador 3': randint(1,6), 
'jogador 4' : randint(1,6)}
ranking={}
for k, v in turma.items():
    print(f' O {k} tirou o valor {v} ')
ranking=sorted(turma.items(),key=itemgetter(1), reverse=True)
print (' O ranking dos jogadores é :')
print(ranking)
for k, v in enumerate(ranking):
    print(f' O {k+1}.o colocado é o {v[0]} tirou que tirou o valor {v[1]} ')
    
