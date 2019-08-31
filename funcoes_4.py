# 8.12

def make_sandwich(*itens):
    """função que agrupa itens do sandwich fornecidos"""
    print("Estes itens são necessários no sanduiche: ")
    for item in itens:
        print("- " + item)


make_sandwich('queijo')
make_sandwich('queijo', 'presunto')
make_sandwich('queijo', 'presunto', 'tomate')


# 8.13
def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um
        usuário."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile_juliano = build_profile('Juliano', 'Cunha',
                                     location='Caxias do Sul',
                                     field='IT',
                                     company='ALGCOM',
                                     age='21'
                                     )
print(user_profile_juliano)


# 8.14
def build_car(manufacturer, model, **car_info):
    """Constroi o dicionário contendo informações sobre o carro selecionado"""
    basic_car = {'car_manufacturer': manufacturer, 'car_model': model}
    for key, value in car_info.items():
        basic_car[key] = value
    return basic_car


car = build_car('subaru', 'impreza',
                color='blue',
                option='boose audio',
                stick='manual'
                )
print(car)
