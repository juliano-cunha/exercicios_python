"""Define uma serie de funções de restaurante"""


class Restaurant():
    """Criando classe restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos da classe"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Utiliza os atributos da classe para descrever o restaurante"""
        print("O nome do restaurante é: " + self.restaurant_name.title() + ".\n" +
              "O restaurante serve comida: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Exibe mensagem de abertura do restaurante"""
        print("O restaurante está aberto")

    def set_number_served(self, atendidos):
        """Define o número de clientes atendidos"""
        self.number_served = atendidos

    def increment_number_served(self, add_atendido):
        """soma o valor de clientes atendidos"""
        self.number_served += add_atendido


        
