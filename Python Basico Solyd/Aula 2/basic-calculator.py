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