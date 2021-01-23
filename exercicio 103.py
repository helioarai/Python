

def cadastro (jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols no campeonato')


jog = str(input('Insira o nome do jogador : '))
ngol= str(input('Insira o número de gols que ele fez no campeonato'))
if ngol.isnumeric():
    ngol=int(ngol)
else :
    ngol=0
if jog.strip()=='':
    cadastro(gols=ngol)
else :
    cadastro (jog,ngol)