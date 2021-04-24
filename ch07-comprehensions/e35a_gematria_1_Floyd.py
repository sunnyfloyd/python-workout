from string import ascii_lowercase

def gematria_dict():
    return {letter: i for i, letter in enumerate(ascii_lowercase, 1)}


def read_config(config):
    return {
        line.split('=')[0]: line.split('=')[1].strip()
        for line in open(config)
    }


# print(read_config('ch07-comprehensions\config_example.txt'))


def read_config_int(config):
    return {
        line.split('=')[0]: int(line.split('=')[1].strip())
        for line in open(config)
        if line.split('=')[1].strip().isdigit()
    }


print(read_config_int('ch07-comprehensions\config_example.txt'))

import json


def cities(json_file):
    # return {
    #     d['city']: d['population']
    #     for d in json.load(open(json_file))
    # }
    return {
        (d['state'], d['city']): d['population']
        for d in json.load(open(json_file))
    }


print(cities('ch07-comprehensions\cities.json'))
print(len(cities('ch07-comprehensions\cities.json')))
