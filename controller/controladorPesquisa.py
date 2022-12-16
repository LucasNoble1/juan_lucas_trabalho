from model.pesquisa import Pesquisa
#from DAOs.cursoDAO import CursoDAO
from view.telaPesquisa import TelaPesquisa


class ControladorPesquisa():
    def __init__(self):
        #self.__curso_dao = CursoDAO()
        self.__pesquisa = Pesquisa()
        self.__tela = TelaPesquisa(self)

    def tela_pesquisa(self):
        self.__tela.tela_opcoes()


    def add_cpf_curso(self, curso, cpf):
        if curso in self.__pesquisa.curso:
            lista = self.__pesquisa.curso[curso]
            lista.append(cpf)
            self.__pesquisa.curso[curso] = lista
            print(self.__pesquisa.curso)
        else:
            self.__pesquisa.curso[curso] = [cpf]
            print(self.__pesquisa.curso)


    def alterar_cpf_curso(self, curso, novo_curso, cpf):
        self.excluir_cpf_curso(curso, cpf)
        self.add_cpf_curso(novo_curso, cpf)

    def excluir_cpf_curso(self, curso, cpf):
        lista = self.__pesquisa.curso[curso]
        lista.remove(cpf)
        if len(lista) == 0:
            del self.__pesquisa.curso[curso]
        else:
            self.__pesquisa.curso[curso] = lista

    def verifica_idade(self,idade):
        if type(idade) == int:
            if idade < 18:
                return "<18"
            if idade >= 18 and idade < 30:
                return "18a29"
            if idade >= 30 and idade < 40:
                return "30a39"
            if idade >= 40 and idade < 50:
                return "40a49"
            if idade >= 50:
                return ">=50"
        else:
            return idade

    def add_cpf_idade(self, idade, cpf):
        chave_idade = self.verifica_idade(idade)
        print(chave_idade)
        lista = self.__pesquisa.idade[chave_idade]
        lista.append(cpf)
        self.__pesquisa.idade[chave_idade] = lista
        print(self.__pesquisa.idade)

    def alterar_cpf_idade(self, idade, nova_idade, cpf):
        self.excluir_cpf_idade(idade, cpf)
        self.add_cpf_idade(nova_idade, cpf)

    def excluir_cpf_idade(self, idade, cpf):
        chave_idade = self.verifica_idade(idade)
        lista = self.__pesquisa.idade[chave_idade]
        lista.remove(cpf)
        self.__pesquisa.idade[chave_idade] = lista


    def add_cpf_ano_ingresso(self, ano_ingresso, cpf):
        if ano_ingresso in self.__pesquisa.ano_ingresso:
            lista = self.__pesquisa.ano_ingresso[ano_ingresso]
            lista.append(cpf)
            self.__pesquisa.ano_ingresso[ano_ingresso] = lista
            print(self.__pesquisa.ano_ingresso)
        else:
            self.__pesquisa.ano_ingresso[ano_ingresso] = [cpf]
            print(self.__pesquisa.ano_ingresso)
    def alterar_cpf_ano_ingresso(self, ano_ingresso, novo_ano_ingresso, cpf):
        self.excluir_cpf_ano_ingresso(ano_ingresso, cpf)
        self.add_cpf_ano_ingresso(novo_ano_ingresso, cpf)

    def excluir_cpf_ano_ingresso(self, ano_ingresso, cpf):
        lista = self.__pesquisa.ano_ingresso[ano_ingresso]
        lista.remove(cpf)
        self.__pesquisa.ano_ingresso[ano_ingresso] = lista
