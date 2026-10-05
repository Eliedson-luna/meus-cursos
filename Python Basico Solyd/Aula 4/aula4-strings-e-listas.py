# Cada item de uma string é um elemento de uma lista, então podemos acessar cada elemento da string como se fosse uma lista.
frase = "Essa frase é uma lista"

print("Segundo item da lista: ",frase[1])

# podemos declarar uma lista de strings utilizando colchetes [].

lista_nomes = ["Anré", "Márcio", "Ana Paula", "Ravi"]

for nome in lista_nomes:
    print(nome)

# podemos declarar uma lista de tipos misturados, como strings, inteiros, booleanos, etc.

lista_mista = ["André", 25, True, 3.14]

for item in lista_mista:
    print(item)


# Alem de escolher um unico item de uma lista, podemos escolher um intervalo de itens utilizando o operador de fatiamento [:].

print("Do segundo ao quarto item da lista: ", lista_nomes[1:4])

# Podemos adicionar um terceiro operador no fatiamento, que é o passo, que indica de quanto em quanto queremos pegar os elementos da lista.

print("Do segundo ao quarto item da lista, de 2 em 2: ", lista_nomes[1:4:2])

## ou se quisermos colocar a lista de trás para frente, podemos utilizar o passo -1.

print("Lista de trás para frente: ", lista_nomes[::-1])
