def get_sv(file_name):
    vowels = set('aeoui')
    return set(
        word.strip()
        for word in open(file_name)
        if vowels < set(word.lower())
    )


# print(get_sv('ch07-comprehensions\words.txt'))

from collections import defaultdict


def different_shells(file_name):
    # Trying to make shell -> users dict
    # output = defaultdict(list)
    # for line in open(file_name):
    #     params = line.split(':')
    #     if len(params) > 1:
    #         output[params[-1].strip()].append(params[0].strip())
    # return output
    return {log.split(':')[-1].strip()
            for log in open(file_name)
            if len(log.split(':')) > 1}


# print(different_shells('ch07-comprehensions\pswd.txt'))


def word_length(file_name):
    # return set(
    #     len(word.strip())
    #     for line in open(file_name)
    #         for word in line.split()
    # )
    # return set(map(len, [
    #     word.strip()
    #     for line in open(file_name)
    #         for word in line.split()
    #     ]))
    return set(map(len, ' '.join(open(file_name)).replace('\n', '').split()))


# print(word_length('ch07-comprehensions\words.txt'))

family_names = [
    'Maciej',
    'Justyna',
    'Lucyna',
    'Maria',
    'Zofia',
    'Grzegorz',
    'Beata',
    'Renata',
    'Anika',
    'Karolina',
    'Martyna',
    'Mateusz'
    ]


def letters_in_names():
    return set(
        letter.lower()
        for name in family_names
            for letter in name)


print(letters_in_names())