from collections import Counter
from os import makedirs


def wordcount(filename):
    params = {'characters': 0, 'words': 0, 'lines': 0, 'unique words': set()}
    with open(filename) as f:
        for line in f:
            params['characters'] += len(line)
            params['words'] += len(line.split())
            params['lines'] += 1
            params['unique words'] = params['unique words'].union(set(line.split()))
            
    params['unique words'] = len(params['unique words'])
    for param_name, param_value in params.items():
        print(f'{param_name}: {param_value}')

# wordcount('ch05-files\wcfile.txt')

import string


def count_certain_words():
    filename = input('Provide name of the file: ')
    words = input('Provide list of names to count: ').split()
    c = Counter()

    with open('ch05-files\\' + filename + '.txt') as f:
        for line in f:
            line = line.translate(str.maketrans('', '', string.punctuation))
            c.update(line.split())

    for word in words:
        print(f'{word}: {c.get(word, 0)}')


# count_certain_words()

import os
import glob
from string import ascii_lowercase


def file_sizes(path):
    file_stats = {file.split('\\')[-1]: os.stat(file).st_size
                    for file in glob.glob(f'{path}/*') if os.path.isfile(file)}
    print(file_stats)

# file_sizes('C:\\Users\\mdebs\\Documents\\GitHub\\python-workout\\ch05-files')

def most_common_letters(path):
    c = Counter()
    for file in glob.glob(f'{path}/*'):
        if not file.endswith('.txt'):
            continue
        with open(file) as f:
            for line in f:
                c.update(line.lower())
    output = Counter({k: v for k, v in c.items() if k in ascii_lowercase})
    print(output.most_common(5))

most_common_letters('C:\\Users\\mdebs\\Documents\\GitHub\\python-workout\\ch05-files')
