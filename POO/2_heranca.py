class Pessoas:
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Estou falando')

class Cliente(Pessoas):
    def comprar(self):
        print('Estou coprando')

class Vendedor(Pessoas):
    def vender(self):
        print('Estou vendendo')

v1 = Vendedor()
v1.vender()