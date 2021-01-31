def get_final_line(file):
    with open(file) as f:
        lines = f.readlines()
        return lines[-1] if lines else ''

def integer_sum_from_text(file):
    with open(file) as f:
        s = 0
        for line in f:
            for chunk in line.split():
                try:
                    s += int(chunk)
                except:
                    pass
        return s

def sum_columns(file):
    total = 0
    with open(file) as f:
        for line in f:
            numbers = line.strip().split('\t')
            if len(numbers) == 2:
                if all(map(str.isdigit, numbers)):
                    total += int(numbers[0]) * int(numbers[1])
    return total


# print(sum_columns('ch05-files\\numbers.txt'))

