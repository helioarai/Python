
cadastro={}
golpart=[]
cadastro['nome']=str(input('Nome do jogador : '))
numpart=int(input(f'Número de partidas disputadas pelo {cadastro["nome"]} : '))
for i in range (0,numpart):
    golpart.append(int(input(f'Gols marcados na partida {i+1} : ')))

cadastro['totgols'] = sum(golpart)
cadastro['gols']=golpart[:]
print(f'O jogador {cadastro["nome"]} jogou {len(cadastro["gols"])} partidas')
for k,v in enumerate (cadastro['gols']):
    print(f'O jogador {cadastro["nome"]} fez na {k+1}.a partida {v} gols ')
print('=+='*30)    
print(f'O total de gols feito nesta temporada pelo jogador {cadastro["nome"]} foi de {cadastro["totgols"]} gols')
print(cadastro)
