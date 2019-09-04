# 9.12 pág 272
"""Possui algumas classes referentes a usuários"""
from user_module import User


class Admin(User):
    """Subclasse da classe User"""

    def __init__(self, first_name, last_name, telefone, email):
        """inicializa os atributo da classe pao"""
        super().__init__(first_name, last_name, telefone, email)


class Privileges(Admin):
    """subaclasse de Admin"""

    def __init__(self, first_name, last_name, telefone, email):
        """inicializa os atributos da classe pai"""
        super().__init__(first_name, last_name, telefone, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """msotra os privilegios"""
        print("Estes são os privilégios de administrador: " + str(self.privileges))