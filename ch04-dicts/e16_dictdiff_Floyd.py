def dictdiff(d1, d2):
    diff = dict()
    for k in dict(d1, **d2):
        if d1.get(k) != d2.get(k):
            diff[k] = [d1.get(k), d2.get(k)]
    return diff


def combine_dicts(*dicts):
    output = dicts[0]
    for d in dicts[1:]:
        d.update(output)
        output = d
    return output


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 3, 'b': 1, 'd': 4}
d3 = {'a': 4, 'g': 0, 'd': 12}
# print(combine_dicts(d1, d2, d3))


def dumbo_dict(*args):
    if len(args) % 2 != 0:
        raise ValueError('There must be an equal number of keys and values passed as the function arguments')
    keys = [key for key in args[::2]]
    values = [value for value in args[1::2]]
    return {k:v for k, v in zip(keys, values)}


print(dumbo_dict('a', 1, 'b', 2, 4, 'a'))


def dict_partition(d, foo):
    left = {}
    right = {}
    for k, v in d.items():
        if foo(k, v):
            left[k] = v
        else:
            right[k] = v
    return (left, right)
