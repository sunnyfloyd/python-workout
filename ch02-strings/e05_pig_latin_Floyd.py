def pig_latin(input_sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    output_sentence = [ f'{word}way' if word[0] in vowels else f'{word[1:]}{word[0]}ay'
                        for word in input_sentence.lower().split()]
    output_sentence = [ output_sentence[i].capitalize() if word[0].isupper() else output_sentence[i]
                        for i, word in enumerate(input_sentence.split())]

    return ' '.join(output_sentence)

pl_sentence = pig_latin # for unit testing

from pathlib import Path

def random_gibberish():
    p = 'C:\\Users\\mdebs\\Documents\\GitHub\\python-workout\\ch02-strings\\random_gibberish.txt'
    lines = ''
    with open(p) as file:
        lines = file.readlines()

    output = []
    for i in range(10):
        output.append(lines[i].split()[i])
    return ' '.join(output)

# print(random_gibberish())

def string_transpose(strings):
    strings = [s.split() for s in strings]
    transposed = [' '.join(x) for x in zip(*strings)]
    return transposed

print(string_transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))