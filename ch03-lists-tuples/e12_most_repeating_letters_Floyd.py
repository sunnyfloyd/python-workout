from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_count(word):
    counter = Counter(word)
    return counter.most_common(1)[0][1]

def most_repeating_word(words):
    max_letter_count = 0
    for word in words:
        c = most_repeating_letter_count(word)
        if c > max_letter_count:
            max_letter_count, w = c, word
    return w
