# podemos interpretar argumentos no terminal usando o módulo sys

import sys

# sys.argv é uma lista que contém os argumentos passados na linha de comando

print("Argumentos: ",sys.argv)

# Exemplo de sudo - Calculadora em linha de comando

import operator

args = sys.argv

flag_list = ["--soma","--subt","--multi", "--divi"]

operator_dic = {
        "--soma": operator.add,
        "--subt": operator.sub,
        "--multi": operator.mul,
        "--divi": operator.truediv
    }


arg_dic = {
    "operator": 0,
    "val_1": 0,
    "val_2": 0
}


help_message = "\n" \
"Uso:\n" \
"   [opcao] [valor_1] [valor_2]" \
"\n\n" \
"Opcoes:\n" \
"   --soma:  soma ambos os valores\n" \
"   --subt:  subtrai o segundo do primeiro\n" \
"   --multi: multiplica um pelo outro\n" \
"   --divi:  divide o primeiro pelo segundo\n"


def load_args():
    if len(args) < 2 or args[0] == "--help":
        print(help_message)
        exit()
    if args[1] in flag_list:
        arg_dic["operator"] = args[1]
    else:
        raise IndexError("Opcao Inválida")
    if args[2].isnumeric():
        arg_dic["val_1"] = float(args[2])
    else:
        raise IndexError("Primeiro valor inválido")
    if args[3].isnumeric():
        arg_dic["val_2"] = float(args[3])
    else:
        raise IndexError("Segundo valor inválido")

def make_result(first_num, opr, second_num):
    result = operator_dic[opr](first_num,second_num)
    return result

try:
    load_args()
except IndexError as e:
    print(e)
    exit()

result = make_result(arg_dic["val_1"], arg_dic["operator"], arg_dic["val_2"])

print("Resultado: ", result)