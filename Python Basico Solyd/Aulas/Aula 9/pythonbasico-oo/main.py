from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 125)

print(caminhao_rosa)
print(type(caminhao_rosa))

print(caminhao_rosa.load_info())


carro_azul = Carro('azul', 'ford', 80)

print(carro_azul.load_info())

carro_azul.abastecer(20)

print(carro_azul.load_info())