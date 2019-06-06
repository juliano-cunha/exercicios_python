#8.6
def city_country(city, country):
    '''Função para escolhe cidades e paises'''
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

    cidadesepaises = city_country(city, country)
    print("A cidade e país  escolhidos foram: " + cidadesepaises)

#8.7
def make_album(artista, titulo, faixas=" "):
    '''Função que define dicionarios para albuns de artistas'''
    album = {
    'artista': 'slash',
    'artista': 'metallica',
    'artista': 'kurt'

     }
