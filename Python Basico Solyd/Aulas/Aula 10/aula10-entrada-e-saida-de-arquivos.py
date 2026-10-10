# Arquivos de Texto

# Podemos abrir um arquivo de texto usando o metodo open(), para isso passamos dois parametros na chamada do mesmo, 
# primeiro o caminho para o arquivo que desejamos abrir, segundo o tipo de operacao que desejamos fazer. 

# no código abaixo podemos ver as operacoes de ecrita (w) e leitura (r) sendo utilizadas.

file = open('arquivo.txt', 'w')

file.write('texto a ser escrito\n')

print(file)

for i in range(0,11):
    file.write(str(i)+"\n")

file.close()

file_read = open('arquivo.txt', 'r')

print("\nPrinting with read():\n")

print(file_read.read())

# Após o read() rodar, o ponteiro/cursor ficará no fim do arquivo, isso significa que se tentarmos ler o aruqivo novamente
# nada será retornado pois já estamos no final do texto. Para resolver isso posicionamos o ponteiro no inicio do arquivo,
# possibilitando uma nova leitura

# > Outra solucao seria fechar e abrir o arquivo novamente.

file_read.seek(0)

print("\nPrinting with for:\n")

for line in file_read:
    print(line)

# Arquivos Binários

img_file = open('test.png', 'rb')

