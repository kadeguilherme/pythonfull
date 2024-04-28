#Criando a classe
class Pessoas:
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

#Criando instancia
p1 = Pessoas('Caio', 21, '123-456-789')
p2 = Pessoas('Marcos', 25, 'xxx-xxx-xxx')

print(p1)
print(p1.nome)
print(p2.nome)

#Print metodos
p1.logar_sistema()
