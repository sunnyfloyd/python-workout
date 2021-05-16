class Animal:
    def __init__(self, color) -> None:
        self.color = color
        self.species = self.__class__.__name__

    def __repr__(self) -> str:
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    number_of_legs = 4


class Sheep(Animal):
    number_of_legs = 4


class Snake(Animal):
    number_of_legs = 0


class Parrot(Animal):
    number_of_legs = 2



w = Wolf('black')
print(w)
w = Sheep('white')
print(w)
w = Snake('blac')
print(w)
w = Parrot('blac')
print(w)