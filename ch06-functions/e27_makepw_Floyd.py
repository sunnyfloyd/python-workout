import random


def create_password_generator(characters):
    def create_password(pw_len):
        return ''.join(random.choice(characters) for _ in range(pw_len))
    return create_password


# alpha_password = create_password_generator('abcdef')
# symbol_password = create_password_generator('!@#$%')
# print(alpha_password(5))
# print(alpha_password(10))
# print(symbol_password(5))
# print(symbol_password(10))

from string import ascii_uppercase, ascii_lowercase, punctuation, digits


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    params_min = [min_uppercase, min_lowercase, min_punctuation, min_digits]
    def check_password(password):
        params_base = [ascii_uppercase, ascii_lowercase, punctuation, digits]
        for param_min, base in zip(params_min, params_base):
            if param_min > sum(True for char in password if char in base):
                return False
        return True
    return check_password


# pw_checker = create_password_checker(2, 4, 1, 3)
# pws = ['AnacondA.123', 'AnacondA.13', 'AnacondA.1234', 'AnacondA123', 'Anacond.-123']
# for p in pws:
#     print(p, pw_checker(p))


def getitem(item):
    def f(collection):
        return collection[item]
    return f


item_getter = getitem('b')
d = {'a':1, 'b':2}
print(item_getter(d))


def doboth(f1, f2):
    def inner(x):
        return f2(f1(x))
    return inner
