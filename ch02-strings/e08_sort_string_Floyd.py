from collections import Counter

def strsort(input_string):
    cnt = Counter(input_string)
    ord_chars = {ord(c):c for c in cnt.keys()}
    sorted_ords = sorted(ord_chars.keys())
    return ''.join(ord_chars[o] * cnt[ord_chars[o]] for o in sorted_ords)

def sort_name(input_name):
    return ','.join(sorted(input_name.split()))

# print(sort_name('Tom Dick Harry'))

def last_word(input_file):
    return sorted(input_file.split())[-1]

print(last_word('kabuba, abura, zanaga, zzaraza, yara, dzumandzi'))