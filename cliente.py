class Cliente():
    def __init__(self, nome, id, email, fone):
        self.set_nome(nome)
        self.set_id(id)
        self.set_email(email)
        self.set_fone(fone)

    def __str__(self):
        return f"{self.__nome} - {self.__id} - {self.__email} - {self.__fone}"

    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id          
    def get_email(self):
        return self.__email    
    def get_fone(self):
        return self.__fone

    def set_nome(self,nome):
        self.__nome = nome
    def set_id(self,id):
        self.__id = id
    def set_email(self,email):
        self.__email = email
    def set_fone(self,fone):
        self.__fone = fone

    def to_json(self):
        dic = { "nome": self.__nome, "id": self.__id, "email": self.__email, "fone": self.__fone}
        return dic

    @staticmethod
    def from_json(dic):
        return Cliente(dic["nome"], dic['id'], dic['email'], dic['fone'])


                            