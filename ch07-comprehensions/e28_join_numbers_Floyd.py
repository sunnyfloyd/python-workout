def join_numbers(range_):
    return ','.join(str(x) for x in range_)


def join_under_10(range_):
    return '.'.join(str(x)
                    for x in range_
                    if 0 <= x <= 10)


def sum_hex(numbers):
    return sum(int(number, 16) for number in numbers)


def reverse_text(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    with open(file_name, 'w') as f:
        f.writelines(f'{line.strip()}\n' for line in lines[::-1])


def reverse_words(file_name):
    return [' '.join(reversed(line.strip().split()))
                    for line in open(file_name)]


# reverse_text('ch07-comprehensions\\reverse_me.txt')
# print(reverse_words('ch07-comprehensions\\reverse_me.txt'))



