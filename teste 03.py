Manipulando texto ou string
frase[9](Acha o nono caractere)
frase[9:13](Do nove ao 12)
frase[3:20:2](Do 3 ao 19 de 2 em 2)
*QUANDO NÃO TEM NADA ANTES DEPOIS OU ENTRE OS DOIS PONTOS A GENTE ASSUME DESDE DE O INÍCIO OU ATE O FINAL DA FRASE RESPECTIVAMENTE
-Fatiamento
-Análise{-len(comprimento);len(frase)
        {-count(conta o num de caracteres);frase.count('o',0,13)
        {-find(diz em que momento começou o 'deo' por exemplo);frase.find('deo')
        {-in(diz se existe ou n o texto buscado na frase);'oi'infrase
-Transformação{-replace(substitui uma palavra por outra);frase.replace('python','android')
              {-upper(transforma tudo pra maiúscula);frase.upper()
              {-lower(transforma tudo pra minúscula);frase.lower()
              {-capitalize(transforma tudo pra minúscula exceto a primeira letra da frase);frase.capitalize()
              {-title(analisa quantas palavras tem na frase fazendo o capitalize palavra por palavra);frase.title()
              {-strip(Remove espaços desnecessários da frase);frase.strip()
              {-rstrip(Remove espaços desnecessários no final da frase);frase.rstrip()=lstrip(faz o contrario)
-Divisão{-split(divide as palavras refazendo os indíces);frase.split()
-Junção{-join(junta todos os elementos de frase usando tal separador selecionado);'-'.join(frase) 
