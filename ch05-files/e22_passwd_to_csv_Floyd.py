import csv


def passwd_to_csv(passwd_filename, csv_filename):
    with open(csv_filename, 'w', newline='') as f:
        o = csv.writer(f, delimiter='\t')
        for line in open(passwd_filename):
            line = line.split(':')
            if len(line) < 3:
                continue
            o.writerow([line[0], line[2]])


# passwd_to_csv('ch05-files\pswd.txt', 'ch05-files\passwd_mine.csv')
# 'passwd_mine.csv'

def passwd_to_csv(passwd_filename, csv_filename, parameters, delimiter):
    with open(passwd_filename) as pwd, open(csv_filename, 'w', newline='') as csvfile:
        input_file = csv.reader(pwd, delimiter=':')
        output_file = csv.writer(csvfile, delimiter=delimiter)
        
        for row in input_file:
            if len(row) >= 3:
                output_file.writerow((row[x] for x in parameters))


# passwd_to_csv('ch05-files\pswd.txt', 'ch05-files\passwd_mine.csv', [0, 2, 3], ';')

def dict_to_csv(d, csv_filename):
    with open(csv_filename, 'w', newline='') as f:
        csv_file = csv.writer(f, delimiter=';')
        for k,v in d.items():
            csv_file.writerow((k, v, repr(type(v))))

# d = {'a': 1, 'ffg': 'fs', 'geez': 122, 'dsfs': 0.2}
# dict_to_csv(d, 'ch05-files\passwd_mine.csv')


import random

def random_csv(csv_filename):
    try:
        with open(csv_filename) as f:
            csv_file = csv.reader(f, delimiter=';')
            for i, row in enumerate(csv_file):
                sum_row = sum(map(int, row))
                print(f'Sum of {i} row is:  {sum_row}')
                print(f'Mean of {i} row is:  {sum_row/len(row)}')
    except IOError:
        with open(csv_filename, 'w', newline='') as f:
            csv_file = csv.writer(f, delimiter=';')
            for i in range(100):
                row = []
                for j in range(10):
                    row.append(random.randint(10, 100))
                csv_file.writerow(row)


random_csv('ch05-files\quick_calc_random.csv')