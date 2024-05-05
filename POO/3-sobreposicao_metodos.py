class Pessoas:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoas):
    def __init__(self, id_client, nome, cpf):
        super().__init__(nome, cpf)
        self.id_client = id_client

class Vendedor(Pessoas):
    def __init__(self, id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor

c1 = Cliente(2, "Guilherme", "123-456-89")

v1 = Vendedor(10, "Roberto", "xxx-xxx-xx")

print(c1.id_client)
print(c1.nome)


print(v1.id_vendedor)
print(v1.nome)