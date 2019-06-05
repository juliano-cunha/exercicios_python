#7.4

prompt = "\nInsira um ingrediente na sua pizza"
prompt += "\nescreva 'quit' para finalizar o programa. "

active = True
while active:
    ingrediente = input(prompt)
    if ingrediente == 'quit':
        active = False
    else:
        print("\nEste ingrediente foi adcionado na sua pizza: " + ingrediente + ".")


#7.5
prompt = input("\n Informe sua idade: ")
active = True
while active:
    idade = int(prompt)
    if idade < 3:
        print("O seu ingresso é gratuito")
        active = False
    elif (idade >= 3) & (idade <= 12):
        print("O seu ingresso  10$")
        active = False
    elif idade > 12:
        print("O seu ingresso custa 15$")
        active = False
    else:
        print("não informou uma idade válida")

#7.6(sem flag)
prompt = input("\n Informe sua idade: ")
while True:
    idade = int(prompt)
    if idade < 3:
        print("O seu ingresso é gratuito")
        break
    elif (idade >= 3) & (idade <= 12):
        print("O seu ingresso  10$")
        break
    elif idade > 12:
        print("O seu ingresso custa 15$")
        break
    else:
        print("não informou uma idade válida")
        break

#7.7(infinito)

prompt = input("\n Informe sua idade: ")
while True:
    idade = int(prompt)
    if idade < 3:
        print("O seu ingresso é gratuito")

    elif (idade >= 3) & (idade <= 12):
        print("O seu ingresso  10$")

    elif idade > 12:
        print("O seu ingresso custa 15$")
    else:
        print("não informou uma idade válida")
