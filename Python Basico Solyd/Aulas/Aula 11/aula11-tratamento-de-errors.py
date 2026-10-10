
# Podemos tratar erros no python com try/except, que funciona com a mesma logica do Try/Catch do Java e outras linguagens de programacao

# tratando erro de forma generica

try:
    a = 2 / 0
except:
    print('Ocorreu um erro')

# tratando erro usando a classe Exception declarando variavel (e), dessa forma podemos usar o próprio python para identificar o que aconteceu

try:
    a = 2 / 0
except Exception as e:
    print('ERROR >>>',e)


# tratando erro com a classe que lida com aquele tipo de erro, o codigo para no primeiro except.

try:
    a = 2 / 0
except ZeroDivisionError:
    print('Você tentou dividir por 0, isso gerou um erro')
except Exception as e:
    print('ERROR >>>',e)


