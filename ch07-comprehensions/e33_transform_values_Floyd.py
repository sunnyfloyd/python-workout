def transform_values(func, d):
    # return dict(zip(d.keys(), map(func, d.values())))
    return {k:func(v) for k,v in d.items()}


# d = {'a':1, 'b':2, 'c':3}
# print(transform_values(lambda x: x*x, d))


def transform_values2(func1, func2, d):
    return {k:func1(v) for k,v in d.items() if func2(k, v)}


def passwd_to_dict(file_name):
    return {log.split(':')[0]:log.split(':')[2]
            for log in open(file_name)
            if len(log.split(':')) > 1}


# print(passwd_to_dict('ch07-comprehensions\pswd.txt'))

import glob
from os import path, stat


def file_info(directory):
    return {name.split('\\')[-1]:stat(name).st_size
            for name in glob.glob(directory)
            if path.isfile(name)}

# print(file_info('ch07-comprehensions\*'))
