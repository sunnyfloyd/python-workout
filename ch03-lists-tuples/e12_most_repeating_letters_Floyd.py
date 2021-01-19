from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_count(word):
    counter = Counter(word)
    return counter.most_common(1)[0][1]

def vowels_repeating_count(word):
    vowels = 'aeouiy'
    counts = Counter(word)
    return sum(v for k,v in counts.items() if k in vowels)

def most_repeating_word(words):
    return max(words, key=vowels_repeating_count)

print(most_repeating_word(WORDS))