def ubbi_dubbi(input_word):
    vowels = 'aeiou'
    translated_word = ''.join(f'ub{c}' if c in vowels else c for c in input_word)
    return translated_word.lower() if input_word[0].islower() else translated_word.lower().capitalize()

print(ubbi_dubbi('elephant'))