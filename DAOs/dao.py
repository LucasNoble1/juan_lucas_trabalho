import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, obj):
        cpf = obj.cpf
        self.__cache.update({cpf: obj})
        self.__dump()

    def update(self, obj):
        cpf = obj.cpf
        if cpf in self.get_all():
            del self.get_all()[cpf]
            self.__cache.update({cpf: obj})
            self.__dump()

    def get(self, key):
        if key in self.get_all():
            return self.get_all()[key]
        else:
            return None

    def remove(self, key):
        cpf = obj.cpf
        if cpf in self.get_all():
            del self.get_all()[cpf]
            self.__dump()

    def get_all(self):
        return self.__cache