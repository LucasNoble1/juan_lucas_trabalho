from view.telaAbstract import Tela

class TelaAluno(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    def tela_opcoes(self):
        print("-----Opçoes do Sistema-----")
        print("\n")
        print("1 - Cadastrar aluno")
        print("2 - Selecionar um aluno")
        print("3 - Mostrar todos os alunos")
        print("4 - Pesquisar alunos")
        print("0 - Voltar")
        print("\n")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 4, 0])
        return opcao


    def selecionar_aluno(self):
        cpf = input("digite o codigo de um aluno:")
        return cpf


    def novo_aluno(self):
        while True:
            print("========================")
            nome = input("Digite o nome: ")
            cpf = input("CPF: ")
            idade = input("Idade:  ")
            print("==>Selecione o Curso do Aluno<==")
            print("1 => Administração")
            print("2 => Arquitetura e Urbanismo")
            print("3 => Biologia")
            print("4 => Ciências Contabeis")
            print("5 => Design")
            print("6 => Direito")
            print("7 => Sistemas de informação")
            print("8 => Zootécnia")
            opcao = self.le_num_inteiro("Selecione um Curso:", [1, 2, 3, 4, 5, 6, 7, 8])
            curso = None
            if opcao == 1:
                curso = "Administração"
            elif opcao == 2:
                curso = "Arquitetura e Urbanismo"
            elif opcao == 3:
                curso = "Biologia"
            elif opcao == 4:
                curso = "Ciências Contabeis"
            elif opcao == 5:
                curso = "Design"
            elif opcao == 6:
                curso = "Direito"
            elif opcao == 7:
                curso = "Sistemas de Informação"
            elif opcao == 8:
                curso = "Zootécnia"
            ano_ingresso = input("Ano de ingresso na faculdade : ")
            if cpf == "" or nome == "" or idade == "" or curso == "" or ano_ingresso == "":
                print("Nenhuma informação deve ser deixada em branco!")
            else:
                return nome, cpf, idade, curso, ano_ingresso


    def mostrar_aluno(self, cpf, nome, curso, idade, ano_ingresso):
        print("=======================")
        print("=> Nome: ", nome)
        print("=> CPF: ", cpf)
        print("=> Curso: ", curso)
        print("=> Idade: ", idade)
        print("=> Ano de ingresso na faculdade: ", ano_ingresso)

    def editar_aluno(self , atributo):
        while True:
            print("--- Editar " + atributo + " ---")
            iten_alterado = input("digite um novo " + atributo + ":" )
            if iten_alterado == "":
                print("Nenhuma informação pode ser deixada em branco!")
            else:
                return iten_alterado

    def editar_curso(self, curso_atual):
        curso = curso_atual
        print("--- Tranferência de curso ---")
        print("curso atual: " + curso)
        print("-----------------------------")
        print("1 => Administração")
        print("2 => Arquitetura e Urbanismo")
        print("3 => Biologia")
        print("4 => Ciências Contabeis")
        print("5 => Design")
        print("6 => Direito")
        print("7 => Sistemas de informação")
        print("8 => Zootécnia")
        opcao = self.le_num_inteiro("Selecione um Curso:", [1, 2, 3, 4, 5, 6, 7, 8])
        if opcao == 1:
            curso = "Administração"
        elif opcao == 2:
            curso = "Arquitetura e Urbanismo"
        elif opcao == 3:
            curso = "Biologia"
        elif opcao == 4:
            curso = "Ciências Contabeis"
        elif opcao == 5:
            curso = "Design"
        elif opcao == 6:
            curso = "Direito"
        elif opcao == 7:
            curso = "Sistemas de Informação"
        elif opcao == 8:
            curso = "Zootécnia"
        return curso

    def escolher_edicao(self, nome, curso, idade, ano_ingresso):
        print("=======================")
        print(" 1 => Alterar o Nome: ", nome)
        print(" 2 => Alterar o Curso: ", curso)
        print(" 3 => Alterar a Idade: ", idade)
        print(" 4 => Alterar o Ano de ingresso na faculdade: ", ano_ingresso)
        print(" 5 => EXCLUIR ALUNO")
        print(" 0 => VOLTAR ")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 4, 5, 0])
        return opcao
