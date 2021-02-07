import string

from requests.api import request

def find_longest_word(filename):
    longest_word = ''
    for line in open(filename, encoding='UTF-8'):
        for word in line.lower().split():
            longest_word = word if len(word) > len(longest_word) and word.isalpha() else longest_word
    return longest_word


import glob


def find_all_longest_words(directory):
    return {file.split('\\')[-1]: find_longest_word(file) for file in glob.glob(f'{directory}/*')}


# print(find_longest_word('ch05-files\\books\\43-0.txt'))
# print(find_all_longest_words('ch05-files\\books'))

# print(len('disinterestedness'))
# print(len('misrepresentation'))

import hashlib
import os


def md5_files(directory):
    return {file: hashlib.md5(file.encode()).hexdigest()
                for file in os.listdir(directory)
                    if os.path.isfile(os.path.join(directory, file))}


# print(md5_files('ch05-files\\books'))

import datetime


def mod_time(directory):
    for file in os.listdir(directory):
        print(file)
    print(f'Directory last time used {datetime.date.fromtimestamp(os.stat(directory).st_ctime)}')


# mod_time('ch05-files\\books')

import requests


def response_counts(url):
    response = requests.get(url)
    response.raise_for_status()
    content = response.text.split('\n')
    counts = dict()
    
    # try 'with'
    for line in content:
        try:
            status = line.split('"')[2].strip().split()[0]
            counts[status] = counts.setdefault(status, 0) + 1
        except:
            pass
    return counts



url = 'https://gist.githubusercontent.com/reuven/5875971/raw/0f20d30d9457c1ded3c6c82798946afaf0b82292/mini-access-log.txt'

print(response_counts(url))