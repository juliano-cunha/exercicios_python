# 9.11 pág 272
# 9.12 pág 272
"""Armazena uma serie de classes de usuário"""


class User():
    """Cria classe de usuário"""

    def __init__(self, first_name, last_name, telefone, email):
        """inicializa os atributo da classe"""
        self.first_name = first_name
        self.last_name = last_name
        self.telefone = telefone
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Método com o resumo das informações do usuário"""
        print("RESUMO DO USUÁRIO CADASTRADO")
        print("Nome do usuário: " + self.first_name.title() + ".\n" +
              "Sobrenome: " + self.last_name.title() + ".\n" +
              "Telefone: " + self.telefone.title() + ".\n" +
              "Email: " + self.email + "\n")

    def greet_user(self):
        """Método com a saudação personalizada para o usuário"""
        print(" Olá, usuário " + self.first_name.title() + " foi cadastrado com sucesso utilizando o email " +
              self.email + ".\n")

    def increment_login_attempts(self):
        """incrementa o valor de login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Limpa as tentativas de login"""
        self.login_attempts = 0
