class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self) -> None:
        self.scoops = []


    def add_scoops(self, *flavors):
        for flavor in flavors:
            if len(self.scoops) == self.max_scoops:
                break
            self.scoops.append(flavor)


    def __repr__(self) -> str:
        return '\n'.join(scoop.flavor for scoop in self.scoops)

class BigBowl(Bowl):
    max_scoops = 5


class Envelope:

    def __init__(self, weight, postage) -> None:
        self.postage = postage
        self.weight = weight
        self.was_sent = False

    def send(self):
        if self.postage_needed() == self.postage:
            self.was_sent = True
    
    def add_postage(self, value):
        self.postage += value

    def postage_needed(self):
        return self.weight * 10


class BigEnvelope(Envelope):
    def postage_needed(self):
        return self.weight * 15


class Phone:
    def dial(self, number):
        return f'Call to {number} has been made.'


class SmartPhone(Phone):
    def run_app(self):
        pass

class iPhone(SmartPhone):
    def dial(self, number):
        return super().dial().lower()
        