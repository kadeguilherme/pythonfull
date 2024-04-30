#Criando a classe
class Pessoas:
    #Atribito de classe
    possui_olho = True
    possui_boca = True
    #Metodo construdor
    def __init__(self, nome, idade, cpf):
        #Atributos de instancias (self)
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def retorna_nome(self):
        return self.nome

    #Criando metodo
    def logar_sistema(self):
        print(f'{self.nome} está logando no sistema')
        print(self.retorna_nome())
    #metodo de classe
    @classmethod #decocator
    def andar(cls):
        print("Estou andando")

#Criando instancia
p1 = Pessoas('Caio', 21, '123-456-789')
p2 = Pessoas('Marcos', 25, 'xxx-xxx-xxx')

#Aqui estou mudando apenas da instancia
p1.possui_boca = False

#Aqui estou trocado atribiuto da clase
Pessoas.possui_olho = False

print(p1)
print(p1.nome)
print(p2.nome)

#Print metodos
p1.logar_sistema()

print(p1.possui_boca)
print(p2.possui_boca)
print(p1.possui_olho)
print(p2.possui_olho)