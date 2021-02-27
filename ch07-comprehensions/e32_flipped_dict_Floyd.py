def flipped_dict(d):
    return {v:k for k,v in d.items()}


# d = {'a':1, 'b':2, 'c':3}

def word_vowels(words):
    return {word:len([char for char in word.lower() if char in 'aeoui'])
            for word in words.split()}

# print(word_vowels('this is an easy test'))

import glob

def file_info(directory):
    files = glob.glob(directory)
    return {file:sum(1 for _ in open(file)) for file in files}


# print(file_info('./ch07-comprehensions/*.py'))


def read_config(file_name):
    return {line.split('=')[0]:line.split('=')[1] for line in open(file_name)}
