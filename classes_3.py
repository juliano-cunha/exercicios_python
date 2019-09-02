# 9.4 pág 254
# 9.6 pág 264 - modificações no exercicio


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

# 9.6


class IceCreamStand(Restaurant):
    """Criada classe da sorveteria,herdando os atributos da classe Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """inicializa atributos da classe pai"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'baunilha', 'menta', 'morango']

    def get_flavors(self):
        """metódo para receber a lista de sabores"""
        print("Estes são os sabores de sorvete: " + str(self.flavors) + " \ndisponiveis hoje")


# criada instancia
restaurant = Restaurant('croasonho', 'croassaint')

# apresenta o valor da instancia criada
print("o restaurante chama: " + restaurant.restaurant_name.title() + ".")
print("Serve este tipo de comida: " + restaurant.cuisine_type.title() + ".")
print("Foram servidos: " + str(restaurant.number_served) + ".")

# altera o valor de number_served
restaurant.number_served = 15
print("Novo valor de pessoas servidas: " + str(restaurant.number_served) + ".")

# define o valor de pessoas atendidas através da chamada de metódo
restaurant.set_number_served(30)
print("Valor atualizado com o metódo: " + str(restaurant.number_served))

# chamada de incremento do valor de pessoas atendidas
restaurant.increment_number_served(20)
print("Valor atualizado com o metódo: " + str(restaurant.number_served))

# criada instancia da IceCreamStand(sorveteria)
my_ice_cream = IceCreamStand('sorvelandia', 'sorveteria')
my_ice_cream.get_flavors()


