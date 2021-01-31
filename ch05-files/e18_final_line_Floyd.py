def get_final_line(file):
    with open(file) as f:
        lines = f.readlines()
        return lines[-1] if lines else ''

def integer_sum_from_text(file):
    with open(file) as f:
        s = 0
        for line in f:
            for chunk in line.split():
                try:
                    s += int(chunk)
                except:
                    pass
        return s

def sum_columns(file):
    total = 0
    with open(file) as f:
        for line in f:
            numbers = line.strip().split('\t')
            if len(numbers) == 2:
                if all(map(str.isdigit, numbers)):
                    total += int(numbers[0]) * int(numbers[1])
    return total


# print(sum_columns('ch05-files\\numbers.txt'))


import requests


def count_vowels(url):
    VOWELS = 'aeouiy'
    vowel_counts = {}
    response = requests.get(url)
    response.raise_for_status()
    
    with open('ch05-files\\vowels.txt', 'wb') as f:
        f.write(response.content)

    with open('ch05-files\\vowels.txt') as f:
        for line in f:
            for char in tuple(line.lower()):
                if char in VOWELS:
                    vowel_counts[char] = vowel_counts.setdefault(char, 0) + 1
    return vowel_counts


url = 'https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'
print(count_vowels(url))
