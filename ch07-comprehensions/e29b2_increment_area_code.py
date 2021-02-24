#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 2: increment_area_code"""


def increment_area_code(full_phone_number):
    area_code, phone_number = full_phone_number.split('-', 1)

    if area_code[0] in '012345':
        area_code = str(int(area_code) + 1)

    return f'{area_code}-{phone_number}'


def increment_all_area_codes(area_codes):
    return [increment_area_code(one_phone_number)
            for one_phone_number in area_codes]


import operator


def year_to_months(d):
    d.update({'age_in_months': d['age']*12})
    return d


def age_in_months(people):
    return [dict(**person, age_in_months=person['age']*12)
            for person in people
            if person['age'] <= 20]
    # return [year_to_months(person)
    #         for person in people
    #         if person['age'] <= 20]


people = [
    {'name': 'John', 'age': 21},
    {'name': 'Ann', 'age': 15},
    {'name': 'Kim', 'age': 20},
    {'name': 'Karen', 'age': 31},
    {'name': 'Yu', 'age': 2},
    {'name': 'Mac', 'age': 17},
    {'name': 'Jack', 'age': 7},
]
print(age_in_months(people))