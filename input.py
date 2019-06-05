#7.1

carro = input('Qual carro deseja: ')
print('Deixe em ver se encontro um ' + carro + ' para você')

#7.2

lugares_restaurante = input('Quantas pessoas estão com vocês?: ')
lugares_restaurante = int(lugares_restaurante)
if lugares_restaurante >= 8:
    print('Vocês terão de aguardar por uma mesa maior')
else:
    print('A mesa de vocês está pronta')


#7.3
mult = input('Digite um número multiplo de 10: ')
mult = int(mult)
if mult % 10 == 0:
    print('O número é um múltiplo de 10')
else:
    print('O número informado  não é um múltiplo de 10')

#''' , ''' serve para ignorar um bloco de código
