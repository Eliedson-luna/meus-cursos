from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        super().__init__(cor, 4, marca, tanque)