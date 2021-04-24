class Scoop:

    def __init__(self, flavor):
        self.flavor = flavor
    

def create_scoops():
    scoops = [
        Scoop(flavor)
        for flavor in ['chocolate', 'vanilla', 'persimmon']
    ]

    for scoop in scoops:
        print(scoop.flavor)


class Beverage:
    def __init__(self, name, temperature=75) -> None:
        self.name = name
        self.temperature = temperature

    
class LogFile:
    def __init__(self, filename) -> None:
        self.file = open(filename, 'w')


