class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self) -> None:
        self.scoops = []


    def add_scoops(self, *flavors):
        for flavor in flavors:
            if len(self.scoops) == Bowl.max_scoops:
                break
            self.scoops.append(flavor)


    def __repr__(self) -> str:
        return '\n'.join(scoop.flavor for scoop in self.scoops)


class Person:
    population_count = 0

    def __init__(self) -> None:
        Person.population_count += 1

    def __del__(self) -> None:
        Person.population_count -= 1


class Transaction:
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount