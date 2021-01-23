from datetime import date
cadastro={}
while True:
    cadastro['nome']=str(input('Coloque o nome do funcionário : '))
    nasc=int(input('Coloque o ano de nascimento : '))
    cadastro['idade']=int(date.today().year - nasc)
    cadastro['numero cart']=int(input('Coloque o número da carteira de trabalho : '))
    if cadastro['numero cart']!= 0 :
        cadastro['ano de contratação'] = int(input('Coloque o ano de contratação : '))
        cadastro['salario']=float(input('Coloque o salário do funcionário'))
        cadastro['aposentadoria']= cadastro['idade'] + (cadastro['ano de contratação']+35)-(date.today().year)
    break
for k,v in cadastro.items():
    print(f'--  {k} tem o valor  {v}')