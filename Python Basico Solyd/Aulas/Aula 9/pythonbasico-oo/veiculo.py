class Veiculo:

    def __init__(self,cor,roda,marca,tanque):
        self.cor = cor
        self.roda = roda
        self.marca = marca
        self.tanque = tanque

    def load_info(self):
        return {'cor': self.cor, 'rodas': self.roda, 'marca': self.marca, 'tanque':self.tanque}

    def abastecer(self, litros) :
        self.tanque = self.tanque+litros