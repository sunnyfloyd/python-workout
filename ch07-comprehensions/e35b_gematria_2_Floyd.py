from string import ascii_lowercase

def gematria_for(word):
    word = word.lower()
    return sum( ascii_lowercase.find(char) + 1
                for char in word
                if char.isalpha())


# print(gematria_for('c---.?at'))

# from collections import defaultdict


def gematria_equal_words(input_word):
    word_gematria = gematria_for(input_word)
    return [word.strip()
            for word in open(r'C:\Users\mdebs\Documents\GitHub\python-workout\ch07-comprehensions\words.txt')
            if gematria_for(word.strip()) == word_gematria]
    # gematrias = defaultdict(list)
    # for word in open(r'C:\Users\mdebs\Documents\GitHub\python-workout\ch07-comprehensions\words.txt'):
    #     gematrias[gematria_for(word.strip())].append(word.strip())
    # return gematrias[word_gematria]


# print(gematria_equal_words('cat'))


def dict_f_to_c(dict_of_temps):
    return {
        city: (temp - 32) * 0.5556
        for city, temp in dict_of_temps.items()
    }


def make_book_dict(book_tuples):
    
    return {
        title:{
            'author_first_name': name.split()[0],
            'author_last_name': name.split()[1:],
            'price': price
        }
        for name, title, price in book_tuples
    }


def currency_conversion(currency_dict):
    user_currency = input('Provide your currency: ')
    return {
        currency_code: (currency_price / currency_dict[user_currency])
        for currency_code, currency_price in currency_dict.items()
    }
