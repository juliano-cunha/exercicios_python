# 9.14 pág 274

from random import randint


class Dice():
    """Define as caracteristicas do dado """

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        random_roll = randint(1, self.sides)
        print("O dado de: " + str(self.sides) + " lados  foi lançado e o resultado é: " +
              str(random_roll) + ".\n")


# instancias dos dados criados
d6 = Dice()
d10 = Dice(10)
d20 = Dice(20)

# chamadas das funções
# chamada com o dado de 6 lados
print("Dados de seis lados\n")
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()
d6.roll_dice()

# chamada com o dado de 10 lados
print("Dados de dez lados\n")
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()
d10.roll_dice()

# chamada com o dado de 20 lados
print("Dados de vinte lados\n")
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()
d20.roll_dice()