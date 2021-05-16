class Cage:
    taken_ids = []
    cage_limit = 3

    def __init__(self, id_number) -> None:
        # if id_number in Cage.taken_ids:
        #     raise ValueError('This ID has already been taken.')
        self.id_number = id_number
        Cage.taken_ids.append(self.id_number)
        self.animals = []

    def add_animals(self, *animals):
        for animal in animals:
            if self.cage_limit > len(self.animals):
                self.animals.append(animal)
            else:
                print('Cage limit reached.')
                break

    def __repr__(self) -> str:
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                                    for animal in self.animals)
        return output


class BigCage(Cage):
    cage_limit = 5