

class Pesquisa:
    def __init__(self):
        self.__curso = {}
        self.__idade = {"<18": [], "18a29": [], "30a39": [],
                        "40a49": [], ">50": []}
        self.__ano_ingresso = {}

    @property
    def curso(self):
        return self.__curso

    def idade(self):
        return self.__idade

    def ano_ingresso(self):
        return self.__ano_ingresso
