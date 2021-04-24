import collections

from attr import attributes


def menu(**options):
    while True:
        user_input = input('What object you want to call: ')
        if user_input in options:
            return options[user_input]()

        print('Not a valid option')

# def funca():
#     return 'I am funca'


# def funcb():
#     return 'I am funcb'


# print(menu(a=funca, b=funcb))


if __name__ == '__main__':
    menu(a=print)


a = 1
b = 2
c = 3


def foo():
    return 'I am foo'


def bar():
    return 'I am bar'



__all__ = [a, c, bar]