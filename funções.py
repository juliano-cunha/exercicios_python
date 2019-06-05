#8.1
def display_message():
    '''mostra a mensagem do que estou aprendendo'''
    print("Neste capítulo estou aprendendo sobre as funções e como utiliza-las no python")


display_message()

#8.2
def favorite_book(titulo_livro):
    '''Chama o livro favorito escolhido'''
    print("Um dos meus livros favoritos é " + titulo_livro.title() + ".")


favorite_book('a revolta de atlas')

#8.3
def make_shirt(tamanho, estampa):
    '''função que define tamanho e estampa na camiseta'''
    print("O tamanho escolhido para a camiseta é " + tamanho.title() + ".")
    print("E a frase da estampa é: " + estampa + ".")


make_shirt('m', 'estampa teste da camiseta')

#8.4
def make_shirt(tamanho='m', estampa='eu amo python'):
    '''função que define tamanho e estampa na camiseta'''
    print("O tamanho escolhido para a camiseta é " + tamanho.title() + ".")
    print("E a frase da estampa é: " + estampa + ".")


make_shirt()
make_shirt('g')
make_shirt('p', 'Minhas funções foram escritas corretamente')

#8.5
def describe_city(cidade, pais= 'brasil'):
    '''Função que descreve a cidade e o pais de um programa'''
    print("O " + pais.title() + " É um pais muito bonito.")
    print("Uma de suas cidades se chama: " + cidade.title() + ".")


describe_city('sao paulo')
describe_city('caxias')
describe_city('madrid', 'espanha')
