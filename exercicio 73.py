brasil=('Palmeiras','Santos','Flamengo','Corinhians','Gremio',
'São Paulo', 'Fluminense','Botafogo','Atletico Mineiro', 'Chapecoense',
'Goias', 'Atletico Paranaense','Cruzeiro', 'Vasco da Gama', 'Vitoria',
'Coritiba', 'Bragantino', 'Bahia','CSA', 'Cuiabá')
print(f'Os cinco primeiros classificados são : {brasil[:5]}')
print(f'Os quatro últimos classificados são : {brasil[-4:]}')
print(f'Times em ordem alfabética : {sorted(brasil)}')
print(f'Colocação da Chapecoense é : {brasil.index("Chapecoense")+1} colocação ')