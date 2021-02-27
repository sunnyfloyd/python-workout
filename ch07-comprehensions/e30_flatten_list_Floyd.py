from itertools import chain


def flatten(arr):
    return [e for e in chain(*arr)]
    # return [e
    #         for wrapped in arr
    #           for e in wrapped]


# def isnumber(num):
#     try:
#         int(float(num))
#         return True
#     except:
#         return False


def numbers_filtering(args):
    for arg in chain(*args):
        try:
            yield int(float(arg))
        except:
            pass


def flatten_odd_ints(arr):
    # return [int(e)
    #         for wrapped in arr
    #             for e in wrapped
    #             if str(e).isdigit() and int(e) % 2]
    return [e for e in numbers_filtering(arr) if e % 2]
    # return [int(float(e))
    #         for e in chain(*arr)
    #         if isnumber(e) and int(float(e)) % 2]


# print(flatten_odd_ints([[2,3,7,'a','-2','-3'], ['33', '13.0', '12.0']]))


def grandchildren_names(family_tree):
    return [name
            for family in family_tree.values()
            for name in family]
    #  return [name
    #         for family in family_tree
    #         for name in family_tree[family]]


# family_tree = {'A': ['B','C','D'], 'B': ['F','G']}
# print(grandchildren_names(family_tree))
family_tree = {
    'A': [
            {'name': 'B', 'age': 8},
            {'name': 'C', 'age': 3},
            {'name': 'D', 'age': 11}],
    'B': [
            {'name': 'F', 'age': 21},
            {'name': 'G', 'age': 2}
                ]}


import operator


def sorted_grandchildren(family_tree):
    children = [child for family in family_tree.values()
                        for child in family]
    return [child['name']
            for child in sorted(children, key=operator.itemgetter('age'), reverse=True)]


print(sorted_grandchildren(family_tree))
