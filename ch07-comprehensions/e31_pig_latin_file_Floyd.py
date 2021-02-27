def plword(word):
    vowels = 'aoeui'
    if word[0] in vowels:
        return word + 'way'
    return word[1:] + word[0] + 'ay'


def plfile(file_name):
    return ' '.join(plword(word)
                    for line in open(file_name)
                        for word in line.split())


# print(plfile('ch07-comprehensions\pig_latin.txt'))


def func(word):
    return word


def funcfile(file_name, foo):
    return ' '.join(foo(word)
                    for line in open(file_name)
                        for word in line)


def dicts_to_tuples(dicts):
    return [tuple_ for d in dicts
                for tuple_ in d.items()]


# dicts = [{'a':1, 'b':2}, {'c': 3}, {'d': 4, 'e': 5}]
# print(dicts_to_tuples(dicts))

from collections import Counter


def most_popular_hobbies(people):
    counter = Counter(
        [hobby
            for person in people
                for hobbies in person.values()
                    for hobby in hobbies]
    )
    return counter.most_common(3)


dicts = [
    {'klaus': {'hunting', 'swimming'}},
    {'henry': {'swimming', 'jogging'}},
    {'misty': {'reading'}},
    {'eleonora': {'football', 'hunting'}},
    {'anne': {'video games', 'swimming', 'reading', 'cooking'}},
    {'karl': {'football', 'movies'}},
    {'klaus': {'swimming', 'football'}}
]
print(most_popular_hobbies(dicts))