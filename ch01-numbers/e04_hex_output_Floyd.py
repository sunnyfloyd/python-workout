def hex_output_no_int():
    num = input('Enter a hex number to convert: ')
    num = str(num)[::-1]
    decimal_output = 0

    for i, digit in enumerate(num):
        digit_code = ord(digit.upper())
        if 48 <= digit_code <= 57:
            decimal_output += (digit_code - 48) * 16**i
        elif 65 <= digit_code <= 70:
            decimal_output += (digit_code - 55) * 16**i
    print(decimal_output)


def hex_output():
    num = input('Enter a hex number to convert: ')
    num = str(num)[::-1]
    decimal_output = 0

    for i, digit in enumerate(num):
        decimal_output += int(digit, base=16) * 16**i
    print(decimal_output)


def name_triangle():
    name = input('Provide your name: ')

    for i, letter in enumerate(name):
        mul_letter = letter * (i+1)
        print(mul_letter)