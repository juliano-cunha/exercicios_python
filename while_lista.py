#7.8
'''
sandwich_orders = ['xis da casa', 'vegetariano', 'bacon', 'salada']
finished_sandwiches = []

while sandwich_orders:
    finalizando_sanduiches = sandwich_orders.pop()
    print("O sanduiche " + finalizando_sanduiches.title() + " esta sendo preparado.")
    finished_sandwiches.append(finalizando_sanduiches)

print("\nEstes são todos os sanduiches finalizados.")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

#7.9
sandwich_orders = ['xis da casa', 'pastrami', 'bacon', 'salada', 'pastrami', 'pastrami']
finished_sandwiches = []
print("Estamos com falta do sanduiche pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nEstes são todos os sanduiches finalizados.")
for finished_sandwiche in sandwich_orders:
    print(finished_sandwiche.title())
'''

#7.10 (INACABADO)
print("\nENQUETE: ")
print("\nSe pudesse visitar um lugar do mundo, para onde você iria? ")

enquete_ativa = True
while enquete_ativa:
    resposta = input("\nQual lugar deseja visitar? ")
    resposta[respostas] = respostata
    #quebra do laço
    repetir = input("Outra pessoa deseja responder? (sim/ nao) ")
    if repetir == 'nao':
        enquete_ativa = False
print("\nENQUETE CONCLUÍDA")
for enquete in respostas.items():
    print(enquete.title())


