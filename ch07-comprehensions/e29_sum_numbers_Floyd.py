def sum_numbers(items):
    return sum(int(x) for x in items.split() if x.isdigit())


def comprehensive_line(file_name):
    vowels = 'aeouiy'
    return [line
            for line in open(file_name)
            if len(line) > 20 and any([ True
                                        for vowel in vowels
                                        if vowel in line])]

# print(comprehensive_line('ch07-comprehensions\\reverse_me.txt'))


def new_number(numbers):
    return [f"{number.split('-')[0]}-{number.split('-')[1]}-{number.split('-')[2]}"
    if int(number.split('-')[1][0]) > 5
    else f"{int(number.split('-')[0])+1}-{number.split('-')[1]}-{number.split('-')[2]}"
    for number in numbers]

print(new_number(['123-456-7890', '123-333-4444', '123-777-8888']))