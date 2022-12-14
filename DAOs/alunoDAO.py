from DAOs.dao import DAO
from model.aluno import Aluno

#cada entidade terá uma classe dessa, implementação bem simples.
class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('aluno.pkl')
        self.__cache = []
    #Adiciona aluno
    def add(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno)):
            super().add(aluno)

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno)):
            super().update(aluno)

    #retorna o aluno, dono do cpf (key)
    def get(self, key):
        return super().get(key)

    #remove aluno dono do cpf(key)
    def remove(self, key):
        return super().remove(key)