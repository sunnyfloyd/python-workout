def firstlast(sequence):
    return sequence[:1] + sequence[-1:]

def even_odd_sums(seq):
    return [sum(x for x in seq[::2]), sum(x for x in seq[1::2])]

print(even_odd_sums([10, 20, 30, 40, 50, 60]))

def plus_minus(seq):
    return seq[0] + sum(x for x in seq[1::2]) + sum(-x for x in seq[2::2])

print(plus_minus([10, 20, 30, 40, 50, 60]))


def myzip(*seqs):
    min_len = min(len(s) for s in seqs)
    return [[s[i] for s in seqs] for i in range(min_len)]

# def myzip(*seqs):
#     zipped = []

#     for i in range(len(seqs)):
#         arr = []
#         for s in seqs:
#             arr.append(s[i])
#         zipped.append(arr)
#     return zipped

print(myzip([10, 20,30], 'abc'))