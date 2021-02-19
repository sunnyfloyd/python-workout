import operator

def calc(eq):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }
    op, a, b = eq.split(' ')

    return ops[op](int(a), int(b))


# print(calc('** 3 4'))


def calc_args(eq):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }
    op, *args = eq.split()
    output = int(args[0])

    for arg in args[1:]:
        output = ops[op](output, int(arg))
    return output


# print(calc_args('+ 3 5 7'))


def apply_to_each(foo, iterable):
    # return list(map(foo, iterable))
    return [foo(x) for x in iterable]


# print(apply_to_each(operator.inv, [10, 12]))


def digit_remover(line):
    return ''.join(char for char in line if not char.isdigit())


def transform_line(foo, input_file, output_file):
    with open(input_file) as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            output_f.write(foo(line))


transform_line(digit_remover, 'ch06-functions\map_for_files.txt', 'ch06-functions\output_map.txt')