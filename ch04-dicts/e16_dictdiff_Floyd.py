def dictdiff(d1, d2):
    diff = dict()
    for k in dict(d1, **d2):
        if d1.get(k) != d2.get(k):
            diff[k] = [d1.get(k), d2.get(k)]
    return diff

# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'd':4}

# print(dictdiff(d1, d2))