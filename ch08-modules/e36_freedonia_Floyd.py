province_taxes = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}

def time_percentage(hour):
    return hour/24

def calculate_tax(price, province, hour):
    hour_tax = time_percentage(hour)
    province_tax = province_taxes[province]
    return price * (1 + (hour_tax * province_tax))


from math import inf

brackets = [
    (1000, 0),
    (10000, 0.1),
    (10000, 0.2),
    (inf, 0.5)
]


def tax_brackets(income):
    bracket = 0
    tax_to_pay = 0
    while income > 0:
        tax = brackets[bracket]
        tax_to_pay += min(tax[0], income) * tax[1]
        income -= min(tax[0], income)
        bracket += 1
    return tax_to_pay

# print(tax_brackets(10001))

char_types = {
    'isdigit': str.isdigit,
    'isalpha': str.isalpha,
    'isspace': str.isspace
}


def analyze_string(sentence):
    char_counts = dict.fromkeys(char_types, 0)
    for char in sentence:
        for check_type, func in char_types.items():
            if func(char):
                char_counts[check_type] += 1
                break
    return char_counts


# print(analyze_string('hel1lo 2 2-'))


def dict_from_keys(d, func):
    return {
        key: func(key)
        for key in d
    }


print(dict_from_keys(['a','b','g'], ord))