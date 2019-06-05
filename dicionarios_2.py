#6.7
people = {
    'joao': {
        'first_name': 'Joaozinho',
        'last_name': 'não sei',
        'age': '30',
        'city': 'são paulo',
        },
    'maria': {
        'first_name': 'maria',
        'last_name': 'joaquina',
        'age': '20',
        'city': 'rio de janeiro',
        },
    'serafino': {
        'first_name': 'serafino',
        'last_name': 'correia',
        'age': '35',
        'city': 'sao leopoldo',
        },
    }

for user, valor in people.items():
    print("\nNome  : " + user)
    print("\nSobrenome  : " + valor['last_name'])
    print("\nIdade  : " + valor['age'])
    print("\nCidade  : " + valor['city'])


#6.8
animais_01 = {
        'nome_animal': 'xurumelas',
        'tipo': 'gato',
        'dono': 'pedro',
        }

animais_02 = {
        'nome_animal': 'mimosa',
        'tipo': 'cavalo',
        'dono': 'jaison',
        }

animais_03 = {
        'nome_animal': 'manhosa',
        'tipo': 'vaca',
        'dono': 'joaquina',
        }

pets = [animais_01, animais_02, animais_03]

for valor in pets:
    print(valor)

#6.9
favorite_places = {
    'wica': ['Mcdonalds', 'shopping', 'zero'],
    'bin': ['chile', 'quadra', 'casa'],
    'vini': ['sao marcos', 'bar'],
    }

for nome, value in favorite_places.items():
    print('O ' + nome.title() + ' Prefere estes locais: ')
    for valores_lista in value:
        print('\t' + valores_lista.title() + '.')

#6.10
numeros_favoritos = {
    'pedro': ['10','20','50'],
    'binao': ['111', '11', '1111', '10'],
    'biel': ['10'],
    'enzo': ['10', '33', '35', '40'],
    'salete': ['10', '20',],
    'luizinho': ['12', '15', '17', '40'],
    }

for nome, numero in numeros_favoritos.items():
    print('Os números favoritos de: ' + nome.title() + ' são:')
    for lista_numero in numero:
        print('\t' + lista_numero)

#6.11

cities = {
    'caxias': {
        'country': 'brasil',
        'population': '500000',
        'fact': 'Caxias do sul é chamada de terra da uva e teve a primeira transmissão a cores de televisão',
        },
    'farroupilha': {
        'country': 'brasil',
        'population': '71000',
        'fact': 'Farroupilha é caracterizada por ser o berço da colonização italiana no Rio Grande do Sul',
        },
    'londres': {
        'country': 'united kingdom',
        'population': '8000000',
        'fact': 'Mais de 150 mil pessoas visitam a Abbey Road todos os anos',
        },
    }

for cidades,informacoes in cities.items():
    print("\nCidade : " + cidades)
    print("País: " + informacoes['country'])
    print("População: " + informacoes['population'])
    print("Fatos: " + informacoes['fact'])

#6.12
favorite_places = {
    'wica': ['Mcdonalds', 'shopping', 'zero'],
    'bin': ['chile', 'quadra', 'casa'],
    'salete': ['casa', 'oriental'],
    'luizinho': ['quadra', 'bar', 'rodeio'],
    'juliano': ['casa', 'bar', 'posto', 'cinema'],
    'renan': ['casa', 'bar'],
    'douglas': ['porto alegre', 'faculdade', 'festa'],
    'enzo': ['cinema', 'festa', 'ap', 'bar'],
    }

for nome, value in favorite_places.items():
    print('\nO usuário: ' + nome.title() + ' respondeu que gosta de visitar tais lugares citados abaixo: ')
    for valores_lista in value:
        print('\t' + valores_lista.title() + '.')
