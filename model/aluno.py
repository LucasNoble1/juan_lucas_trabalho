

class Aluno:
    def __init__(self , cpf, nome, curso,ano_de_ingresso, idade):
        self.__cpf = cpf
        self.__nome = nome
        self.__curso = curso
        self.__ano_de_ingresso = ano_de_ingresso
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def curso(self):
        return self.__curso

    @property
    def ano_de_ingresso(self):
        return self.__ano_de_ingresso

    @property
    def idade(self):
        return self.__idade

    #setter
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome

    def set_curso(self, curso):
        self.__curso = curso

    def set_ano_de_ingresso(self, ano):
        self.__ano_de_ingresso = ano

    def set_idade(self, idade):
        self.__idade = idade


