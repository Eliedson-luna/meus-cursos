# Print
print("Aprendendo Print: ")
print('Hello World')

# Variaveis
print("")
print("Variaveis")
print("")

numero = 65
numero_type = type(numero)

nome = "Abilio"
nome_type = type(nome)

print(numero,': ', numero_type, ', ' , nome,': ', nome_type)

print(f"Nome: {nome} type: {nome_type} ")

print(f"Numero: {numero} type: {numero_type} ")

# Alterando Tipos

print("")
print("Alterando Tipos")
print("")

print("> Declarando variavel")

num = 65

print(f"Varivel: {num} tipo: {type(num)}")

print("> Alterando tipo")

num = str(num)

print(f"Variavel: {num} tipo: {type(num)}")

# Inputs 

print("")
print("Inputs")
print("")

num_input = input("insira um numero: ")
print("")

nome_input = input("insira um nome: ")

print(f"num_input: {num_input} tipo: {type(num_input)}")

print(f"nome_input: {nome_input} tipo: {type(nome_input)}")

# Operacoes


print("Operacoes")

# Estou fazendo uma calculadora para dificultar um pouco as coisas rsrs

class Calculator:

    import operator

    
    operator_dic = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    @staticmethod
    def get_num(msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print('nao é um numero')
    
    @staticmethod
    def get_operator():
        while True:
            opr = input("Informe o operador (+, -, *, /): ") 
            if opr in Calculator.operator_dic:
                return opr
            print('operador inválido')

    @staticmethod
    def make_result(first_num, opr, second_num):
        result = Calculator.operator_dic[opr](first_num,second_num)
        return result

    @staticmethod
    def start():

        print ("| Calculadora |")
        print("")

        first_num = Calculator.get_num('1° numero: ')
        print("")
        selected_operator = Calculator.get_operator()
        print("")
        second_num = Calculator.get_num('2° numero: ')
        print("")
        print("Gerando resultado")
        result = Calculator.make_result(first_num, selected_operator, second_num)
        print('Res.: ',result)

Calculator.start()