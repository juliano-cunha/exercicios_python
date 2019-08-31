# 8.6
def city_country(city, country):
    """Função para escolhe cidades e paises"""
    cidadepais = city + " , " + country
    return cidadepais.title()


while True:
    print("Digite o nome de um país e uma cidade: ")
    print("Pressione 's' para sair")

    city = input("Cidade: ")
    if city == 's':
        break

    country = input("País: ")
    if city == 's':
        break

""" bloco ignorado para utilizar as funções no city_country_app_funcoes
    cidadesepaises = city_country(city, country)
    print("A cidade e país  escolhidos foram: " + cidadesepaises)
"""
