from model.pesquisa import Pesquisa
#from DAOs.cursoDAO import CursoDAO


class ControladorPesquisa():
    def __init__(self):
        #self.__curso_dao = CursoDAO()
        self.__pesquisa = Pesquisa()

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
        if idade < 18:
            return "<18"
        if idade >= 18 and idade < 30:
            return "18a29"
        if idade >= 30 and idade < 40:
            return "30a39"
        if idade >= 40 and idade < 50:
            return "40a49"
        if idade >= 50:
            return ">50"

    def add_cpf_idade(self, idade, cpf):
        chave_idade = self.verifica_idade(idade)
        lista = self.__pesquisa.curso[chave_idade]
        lista.append(cpf)
        self.__pesquisa.idade[chave_idade] = lista
        print(self.__pesquisa.idade)

    def alterar_cpf_idade(self, idade, nova_idade, cpf):
        pass
    def excluir_cpf_idade(self, curso, cpf):
        pass


    def add_cpf_ano_ingresso(self, idade, cpf):
        pass
    def alterar_cpf_ano_ingresso(self, idade, nova_idade, cpf):
        pass
    def excluir_cpf_ano_ingresso(self, curso, cpf):
        pass






