from controller import PessoaController
while True:
    decisao = int(input("Digite 1 para salvar a pessoa ou digita 2 para ver a pessoa salva e 3 para sair"))
    if decisao == 3 :
        break
    if decisao ==1:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite seu cpf: ")
        if PessoaController.cadastrar(nome,idade,cpf):
            print("Cadastrado com sucesso")
        else:
            print("Digite valores validos")
    else:
        print("Digite valores validos")