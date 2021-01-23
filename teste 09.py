DICIONÁRIOS
dados = {}
dados = dict()
dados = {'nome':Pedro,'idade':25};nome e idade como se fossem índices
print(dados['nome']} = Pedro
dados['sexo']='M';insere um novo índice no dicionário
del dados['idade'];deleta um índice
filme = {'título':'Star Wars',
         'ano':1977
         'diretor':George Lucas
            }
print(filme.values()) = star wars,1977,george lucas
print(filme.keys()) = titulo,ano,diretor
print(filme.items())
for k,v in filme.items():
    print(f"O {k} é {v}")
O título é Star wars
O ano é 1977
O diretor é George Lucas
*Você pode criar uma lista em que cada elemento seria um dicionário
locadora = ['Star Wars','1977','George Lucas']
             'título'   'ano'    'diretor'
                            1
brasil.append(estado.copy()) = cópia envolvendo dicionário
import operator ; dentro temos o itemgetter que funciona como o sort dos dicionarios
