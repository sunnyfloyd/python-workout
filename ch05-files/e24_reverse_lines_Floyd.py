def reverse_lines(input_file, output_file):
    with open(output_file, 'w') as output:
        for line in open(input_file):
            output.write(line.rstrip()[::-1] + '\n')


# reverse_lines('ch05-files\input.txt', 'ch05-files\output.txt')

def encrypt(filename, text):
    with open(filename, 'w') as f:
        f.write('-'.join(str(ord(char)) for char in text))


def decrypt(filename):
    with open(filename) as f:
        return ''.join(chr(int(char)) for char in f.read().split('-'))

# encrypt('ch05-files\encrypted.txt', '''Encrypted message!
# haha!''')
# print(decrypt('ch05-files\encrypted.txt'))

from collections import defaultdict
from os import write
from string import ascii_lowercase


def vowels_and_consonants(infilename, vowel_filename, consonant_filename):
    vowels = 'aeouiy'
    with open(infilename) as input_file, open(vowel_filename, 'w') as vowel_file, open(consonant_filename, 'w') as consonant_file:
        for line in input_file:
            for char in line:
                if char.lower() in vowels:
                    vowel_file.write(char)
                elif char.lower() in ascii_lowercase:
                    consonant_file.write(char)


# vowels_and_consonants('ch05-files\input.txt', 'ch05-files\\vowels.txt', 'ch05-files\consonants.txt')

from collections import defaultdict


def shell_users(filename, outfilename):
    shells = defaultdict(set)
    with open(filename) as pswd, open(outfilename, 'w', newline='') as output:
        for line in pswd:
            if len(line.split(':')) > 1:
                user = line.split(':')[0]
                shell = line.split(':')[-1].strip()
                shells[shell].add(user)
        for shell, users in shells.items():
            output.write(f"{shell}:{', '.join(list(users))}\n")


shell_users('ch05-files\pswd.txt', 'ch05-files\shell_summary.txt')