 class profissional():

    def__init__(self, nome, id, especialidade, conselho):
        self.set_nome(nome)
        self.set_id(id)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho) 

    def__str__(self):
            return f"{self.__nome} - {self.__id} - {self.__especialidade} - {self.__conselho}"  

    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id          
    def get_especialidade(self):
        return self.__especialidade    
    def get_conselho(self):
        return self.__conselho

    def set_nome(self,nome):
        self.__nome = nome
    def set_id(self,id):
        self.__id = id
    def set_email(self,especialidade):
        self.__especialidade = especialidade
    def set_fone(self,conselho):
        self.__conselho = conselho

    def to_json(self):
        dic{ "nome": sel.__nome, "id": self.__id, "especialidade": self.__especialidade, "conselho": self.__conselho}
        return dic

    @staticmethod
    def from_json(dic):
        return profissional(dic["nome"], dic['id'], dic['especialidade'], dic['conselho'])                           