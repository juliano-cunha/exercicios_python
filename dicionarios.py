#6.1
pessoa_favorita = {
    'first_name': 'Joaozinho',
    'last_name': 'não sei',
    'age': '30',
    'city': 'são paulo',
    }

print("o nome dela é " + pessoa_favorita['first_name'] + " e tem " + pessoa_favorita['age'] + " anos de idade")

#6.2

numeros_favoritos = {
    'pedro': '10',
    'bin': '15',
    'wica': '20',
    'vini': '30',
    'bi': '40',
    'douglas': '12',
    }
print("O numero favorito de pedro é: " + numeros_favoritos['pedro'])
print("O numero favorito de bin é: " + numeros_favoritos['bin'])
print("O numero favorito de wica é: " + numeros_favoritos['wica'])
print("O numero favorito de vini é: " + numeros_favoritos['vini'])
print("O numero favorito de douglas é: " + numeros_favoritos['douglas'])

#6.3

glossario_python = {
    'elif': 'estrutura de testes "se" de forma encadead e indentada no python',
    'chaves_dicionarios': 'utilizado para acessar determinado valor dos pares de dicionarios',
    'indentacao': 'conjunto de espaços utilizados para melhor visualização da estrutura do código ',
    'sintaxe': 'modelo padrão de palavras que forma a estrutura e comandos de determianda linguagem',
    'laço': 'regra que define um agrupamento de informações normalmente utilizado para criar repetições',
    }

print("Significado de elif: " + glossario_python['elif'] + "\n"
        "Significado de chaves dicionarios: " + glossario_python['chaves_dicionarios'] + "\n"
        "Significado de indentação: " + glossario_python['indentacao'] + "\n"
        "Significado de sintaxe: " + glossario_python['sintaxe'] + "\n"
        "Significado de laço: " + glossario_python['laço'] + "\n"
      )

#6.4

glossario_python = {
    'elif': 'estrutura de testes "se" de forma encadead e indentada no python',
    'chaves_dicionarios': 'utilizado para acessar determinado valor dos pares de dicionarios',
    'indentacao': 'conjunto de espaços utilizados para melhor visualização da estrutura do código ',
    'sintaxe': 'modelo padrão de palavras que forma a estrutura e comandos de determianda linguagem',
    'laço': 'regra que define um agrupamento de informações normalmente utilizado para criar repetições',
    '.title': 'Adiciona letra maiuscula na primeir palavra da sentença',
    '.append': 'adiciona mais um item na lista',
    '.items': 'percorre todos os itens do dicionário',
    'set': 'indentifica os itens e seleciona somente os únicos',
    '.order': 'ordena em ordem alfabetica as chaves a valores do dicionário',
    }

for k, v in glossario_python.items():
    print("Significado de " + k + " é: " + v + ".\n")

#6.5

rios_paises = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'prata': 'argentina',
    }

for r in rios_paises.keys():
    print(r.title())

for v in rios_paises.values():
    print(v.title())

#6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'coulson': 'avengers',
    'eduardo': 'java',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin por favor responda o questionário!")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", obrigado por participar.")





