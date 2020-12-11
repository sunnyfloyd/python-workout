def mysum(*args, starting_sum=0):
    s = starting_sum
    for arg in args:
        try:
            arg = iter(arg)
        except TypeError:
            s += arg
        else:
            for a in arg:
                s += a
    return s

print(mysum(2, 3, 4, [1, 2], starting_sum=4))

def avg(*numbers):
    s = 0
    for num in numbers:
        s += num
    return s / len(numbers)

print(avg(5,10,6))

def sente_stats(*sentence):
    shortest = len(sentence[-1])
    longest = len(sentence[-1])
    s = 0

    for word in sentence:
        shortest = len(word) if len(word) < shortest else shortest
        longest = len(word) if len(word) > longest else longest
        s += len(word)
    return (shortest, longest, s / len(sentence))

print(sente_stats('abba', 'karamba', 'si'))

def sum_everything(*args):
    s = 0
    for arg in args:
        try:
            t = int(arg)
        except:
            pass
        else:
            s += t
    return s

print(sum_everything(2, 5, '2', 'w', 1, '100'))