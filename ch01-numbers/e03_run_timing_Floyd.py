def run_timing():
    total_time = 0
    number_of_runs = 0

    while True:
        user_time = input('Enter 10 km run time: ')
        if not user_time:
            break
        total_time += float(user_time)
        number_of_runs += 1
    print(f'Average of {total_time / number_of_runs}, over {number_of_runs} runs')

def cut_floats(f_number: float, before: int, after: int):
    int_part = str(int(f_number))
    int_part = int_part[len(int_part) - before:]
    dec_part = str(f_number % 1)[2:][:after]
    return float(int_part + '.' + dec_part)

# print(cut_floats(1234.5678, 4, 4))

from decimal import *

def correct_float(num1: str, num2: str):
    num1 = Decimal(num1)
    num2 = Decimal(num2)

    return float(num1 + num2)

print(correct_float('0.1', '0.2'))