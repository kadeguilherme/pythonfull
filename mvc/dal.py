from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    def ler(self):
        nome = "Guilherme"
        idade = 23
        cpf = '123'

p1 = Pessoa("Guilherme Aguiar", 24, "xxx-xxx")
PessoaDal.salvar(p1)