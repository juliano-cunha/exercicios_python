# 9.3 pág 248
# 9.5 pág 254 (retomada do exercicio)
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


# Maiusculo é referente a classe
# Criada as instancias de teste
user_1 = User('juliano', 'cunha', '3211-2293', 'julianocunhatrabalho@gmail.com')
user_2 = User('douglas', 'camatti', '3211-2295', 'douglas@gmail.com')
user_3 = User('eduardo', 'bin', '3211-2298', 'eduardo@gmail.com')

# Realizada a chamada dos metódos criados

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()

# chamada da instancia para incrementar o valor de tentativas de login do user_1
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("Número de tentativas de login: " + str(user_1.login_attempts) + ".")

# chamada da instancia para resetar o número de tentativas de login
user_1.reset_login_attempts()
print("Número de tentativas de login resetado : " + str(user_1.login_attempts) + ".")
