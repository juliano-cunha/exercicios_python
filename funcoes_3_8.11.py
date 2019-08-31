def show_magicians(nomes_magicos):
    """Função imprime a lista de magicos"""

    for name in nomes_magicos:
        print(name)

def make_great(nomes_magicos, nomes_magicos_alterados):
    """Função que adiciona o texto grande aos nomes da lista """
    while nomes_magicos:
        alterando_nomes = "o Grande " + nomes_magicos.pop() + "!"
        nomes_magicos_alterados.append(alterando_nomes)


nomes_magicos = ['houdini', 'tony', 'douglas']
nomes_magicos_alterados = []


show_magicians(nomes_magicos[:])
make_great(nomes_magicos, nomes_magicos_alterados)
show_magicians(nomes_magicos_alterados)



