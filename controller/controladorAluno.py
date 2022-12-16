from model.aluno import Aluno
from view.telaAluno import TelaAluno
from DAOs.alunoDAO import AlunoDAO
from controller.controladorPesquisa import ControladorPesquisa

class ControladorAluno:
    def __init__(self):
        self.__tela = TelaAluno(self)
        self.__aluno_dao = AlunoDAO()
        self.__controladorPesquisa = ControladorPesquisa()

    def inicia_sistema(self):
        lista_opcoes = {1: self.add_aluno, 2: self.alterar_aluno,3: self.mostrar_todos,
                        4: self.pesquisar, 0: self.sair}

        continua = True
        while continua:
            lista_opcoes[self.__tela.tela_opcoes()]()


    def add_aluno(self):
        nome, cpf, idade, curso, ano_ingresso = self.__tela.novo_aluno()
        cpf_valido = False
        idade_valido = False
        ano_valido = False
        while cpf_valido == False:
            cpf_valido = True
            if cpf in self.__aluno_dao.get_all():
                self.__tela.mostra_mensagem("CPF JA EXISTE!, INFORME OUTRO CPF!")
                cpf = self.__tela.editar_aluno("cpf")
                cpf_valido = False
            if cpf.isdigit() == False:
                self.__tela.mostra_mensagem("CPF deve conter somente numeros!")
                cpf = self.__tela.editar_aluno("cpf")
                cpf_valido = False

        while idade_valido == False:
            idade_valido = True
            if idade.isdigit() == False :
                self.__tela.mostra_mensagem("Idade deve conter somente numeros!")
                idade = self.__tela.editar_aluno("idade")
                idade_valido = False

        while ano_valido == False:
            ano_valido = True
            if ano_ingresso.isdigit() == False :
                self.__tela.mostra_mensagem("Ano deve conter somente numeros!")
                ano_ingresso = self.__tela.editar_aluno("Ano de ingresso na faculdade")
                ano_valido = False
            if ano_valido == True:
                if int(ano_ingresso) < 1960 or int(ano_ingresso) > 2023:
                    self.__tela.mostra_mensagem("Digite um ano valido!(maior que 1959 e menor que 2024")
                    ano_ingresso = self.__tela.editar_aluno("Ano de ingresso na faculdade")
                    ano_valido = False

        aluno = Aluno(int(cpf), nome, curso, int(ano_ingresso), int(idade))
        self.__aluno_dao.get_all().update({cpf: aluno})
        self.__tela.mostra_mensagem("Aluno incluido com sucesso!")
        self.__controladorPesquisa.add_cpf_curso(curso, cpf)
        self.__controladorPesquisa.add_cpf_idade(int(idade), cpf)
        self.__controladorPesquisa.add_cpf_ano_ingresso(int(ano_ingresso), cpf)


    def alterar_aluno(self):
        cpf = self.__tela.selecionar_aluno()
        terminou = None
        while terminou == None:
            if cpf in self.__aluno_dao.get_all():
                nome = self.__aluno_dao.get_all()[cpf].nome
                idade = self.__aluno_dao.get_all()[cpf].idade
                curso = self.__aluno_dao.get_all()[cpf].curso
                ano_ingresso = self.__aluno_dao.get_all()[cpf].ano_de_ingresso
                opcao = self.__tela.escolher_edicao(nome, curso, idade, ano_ingresso)
                if opcao == 1:
                    edit = self.__tela.editar_aluno("nome")
                    self.__aluno_dao.get_all()[cpf].set_nome(edit)
                elif opcao == 2:
                    edit = self.__tela.editar_curso(curso)
                    self.__aluno_dao.get_all()[cpf].set_curso(edit)
                    self.__controladorPesquisa.alterar_cpf_curso(curso, edit, cpf)
                elif opcao == 3:
                    idade_valido = False
                    while idade_valido == False:
                        edit = self.__tela.editar_aluno("idade")
                        idade_valido = True
                        if edit.isdigit() == False:
                            self.__tela.mostra_mensagem("Idade deve conter somente numeros!")
                            idade_valido = False
                    self.__aluno_dao.get_all()[cpf].set_idade(int(edit))
                    self.__controladorPesquisa.alterar_cpf_idade(idade, int(edit), cpf)
                elif opcao == 4:
                    ano_valido = False
                    while ano_valido == False:
                        ano_valido = True
                        edit = self.__tela.editar_aluno("Ano de ingresso na faculdade")
                        if edit.isdigit() == False:
                            self.__tela.mostra_mensagem("Ano deve conter somente numeros!")
                            ano_valido = False
                        if ano_valido == True:
                            if int(edit) < 1960 or int(edit) > 2023:
                                self.__tela.mostra_mensagem("Digite um ano valido!(maior que 1959 e menor que 2024")
                                ano_valido = False
                    self.__aluno_dao.get_all()[cpf].set_ano_de_ingresso(edit)
                    self.__controladorPesquisa.alterar_cpf_ano_ingresso(int(ano_ingresso),int(edit), cpf)
                elif opcao == 5:
                    terminou = True
                    self.excluir_aluno(cpf)
                elif opcao == 0:
                    terminou = True







    def excluir_aluno(self, cpf):
        curso = self.__aluno_dao.get_all()[cpf].curso
        idade = self.__aluno_dao.get_all()[cpf].idade
        ano_ingresso = self.__aluno_dao.get_all()[cpf].ano_de_ingresso
        del self.__aluno_dao.get_all()[cpf]
        self.__tela.mostra_mensagem("Aluno Excluido com sucesso!")
        self.__controladorPesquisa.excluir_cpf_curso(curso, cpf)
        self.__controladorPesquisa.excluir_cpf_idade(idade, cpf)
        self.__controladorPesquisa.excluir_cpf_ano_ingresso(ano_ingresso, cpf)

    def mostrar_todos(self):
        if len(self.__aluno_dao.get_all()) == 0:
            self.__tela.mostra_mensagem("Nenhum aluno foi cadastrado ainda!")
            self.__tela.pausa()
        else:
            for aluno in self.__aluno_dao.get_all().values():
                nome = aluno.nome
                cpf = aluno.cpf
                idade = aluno.idade
                curso = aluno.curso
                ano_ingresso = aluno.ano_de_ingresso
                self.__tela.mostrar_aluno(cpf, nome, curso, idade, ano_ingresso)
            self.__tela.pausa()



    def pesquisar(self):
        self.__controladorPesquisa.tela_pesquisa()
    def sair(self):
        exit[0]



