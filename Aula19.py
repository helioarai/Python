dados=dict()
dados={'nome':'Eduardo','idade':23}

print(f'O {dados["nome"]} tem {dados["idade"]} anos')
dados['sexo']='M'
#del dados['nome']
dados['nome']='Ferdinando'
print(dados['nome'])
print(dados.keys())
print(dados.values())
print(dados.items())
for k,v in dados.items():
    print (f'{k} = {v}')
brasil =[]
estado1={'uf':'rio de janeiro', 'sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
pais=[]
estado=dict()
for i in range (0,3):
    estado['uf']=str(input('Unidade federativa : '))
    estado['sigla']=str(input('Sigla do estado : '))
    pais.append(estado.copy())
print(pais)
for i in pais :
    for k,v in i.items() :
        print(f'O campo {k} tem o valor{v}')