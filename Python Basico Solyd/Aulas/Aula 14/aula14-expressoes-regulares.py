# Nessa aula utilizamos a biblioteca 're', que é a abreviacao para 'regular expressions', para buscar padroes de texto dentro de strings.

import re

test_string = 'o gato e bonito'

# Utilizamos o 'r' antes do padrao a ser procurado na string para transformar o padrao em 'raw_string', isso quer dizer que parametros como
# '\n', utilizado para pular linha, nao serao lidos como parametros e sim como uma string.

# Erro proposital

pattern = r'gata'

result = re.search(pattern, test_string)

if result:
    print(result.group())
else:
    print('Padrao nao encontrado')

# Econtrando o padrao

pattern_2 = r'gato'

result_2 = re.search(pattern_2, test_string)

if result_2:
    print('Padrao encontrado: ',result_2.group())
else:
    print('Padrao nao encontrado')

# O filtro por padroes nao se limita a palavas completas, podemos utilizar '.' para definir apenas iniciais ou o final de uma palavra 
# ou frase.

# Encontrando a palavra gato atraves das iniciais

pattern = r'gat.' # Fato interessante: sem o '.' o código encontra o padrao 'gat' pesente na palavra 'gato', o que é uma outra forma de
                  # utilizar essa funcionalidade

result = re.search(pattern, test_string)

if result:
    print('Padrao encontrado - iniciais: ',result.group())
else:
    print('Padrao nao encontrado')

# Encontrando a palavra gato atraves das ultimas letras

pattern = r'.ato'

result = re.search(pattern, test_string)

if result:
    print('Padrao encontrado - ultimas letras: ',result.group())
else:
    print('Padrao nao encontrado')

# Encontrando a palavra gato atraves das letras do meio

pattern = r'.at.'

result = re.search(pattern, test_string)

if result:
    print('Padrao encontrado: ',result.group())
else:
    print('Padrao nao encontrado')

# Procurando varios matches com o 'findall()'

test_string = 'o gato, a gata e os gatinhos bonitos'

pattern = r'gat\w+'

result = re.findall(pattern, test_string)

if result:
    print('Padrao encontrado - findall: ',result)
else:
    print('Padrao nao encontrado')

# Procurando padroesde email

email_pattern = r'[\w\.-]+@[\w-]+\.[\w\.-]+'

test_email = 'email@test.com.br'

email_result = re.search(email_pattern, test_email)

print('Padrao encontrado - emal: ',email_result.group())

# Destrinchando a regex 'r'[\w\.-]+@[\w-]+\.[\w\.-]+''

# [] - utilizamos os colchetes quando queremos passar mais de um padrao em um espaço na string, no nosso exemplo o '@' está representando
# um caractere de string mesmo, e o '[\w\.-]+' antes dele significa que estamos filtrando nesse espaço: strings que tenham caracteres em 
# unicode (\w), ponto (\.), traço (-) e o que estiver depois desses padroes (+).

# o mesmo serve para o resto da regex, repare que temos apenas 3 caracteres fixos no padrao: '@', '.' e outro '.'

# Como representar o ponto ('.'):

# para representar o ponto utilizamos uma contrabarra antes dele, uma vez que vimos no inicio que o ponto sozinho serve de parametro para
# a regex. Utilizamos: '\.'
