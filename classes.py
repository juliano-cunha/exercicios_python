# 9.1 pag 248
class Restaurant():
    """Criando classe restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos da classe"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Utiliza os atributos da classe para descrever o restaurante"""
        print("O nome do restaurante é: " + self.restaurant_name.title() + ".\n" +
              "O restaurante serve comida: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """Exibe mensagem de abertura do restaurante"""
        print("O restaurante está aberto")


# R maiusculo é referente a classe
# Criada a instancia restaurant a partir da minha classe
restaurant = Restaurant('croasonho', 'croassaint')

# atributos sendo mostrados individualmente
print("o restaurante chama: " + restaurant.restaurant_name.title() + ".")
print("Serve este tipo de comida: " + restaurant.cuisine_type.title() + ".")

# Chamada dos métodos criados
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2 pag 248 - instanciando mais 3 restaurantes
restaurant_1 = Restaurant('luizinho', 'brasileira')
restaurant_2 = Restaurant('tayo', 'sushi')
restaurant_3 = Restaurant('don romano', 'pizza')

print("\nOutros três restaurante instanciados\n")
# respectivas chamadas dos metódos das novas instancias
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()



