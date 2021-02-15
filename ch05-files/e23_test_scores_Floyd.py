import glob
import json


def print_scores(directory):
    json_files = glob.glob(directory + '\*.json')
    for file in json_files:
        with open(file) as f:
            score_per_subject = {}
            student_scores = json.load(f)
            print(student_scores)

            for subject_scores in student_scores:
                for subject, score in subject_scores.items():
                    score_per_subject.setdefault(subject, []).append(score)
            print('/'.join(file.split('\\')[1:]))

            for subject, scores in score_per_subject.items():
                print(f'\t{subject}: min {min(scores)}, max {max(scores)}, average {sum(scores)/len(scores)}')


# print_scores('ch05-files\scores')

import csv


def json_passwd(filename):
    with open(filename) as pwd:
        output = []
        csv_file = csv.reader(pwd, delimiter=':')

        for row in csv_file:
            if len(row) > 1:
                output.append(tuple(row))
        j = json.dumps(output, indent=4)
        print(j)


# json_passwd('ch05-files\pswd.txt')


def json_passwd_dict(filename):
    keys = [
        'username',
        'password',
        'user ID',
        'group ID',
        'user ID info',
        'home directory',
        'shell'
    ]
    output = []

    for line in open(filename):
        record = line.strip('\n').split(':')
        if len(record) > 1:
            output.append(dict(zip(keys, record[:4] + record[7:])))
    
    print(json.dumps(output, indent=4))


# json_passwd_dict('ch05-files\pswd.txt')

from os import stat, path


def write_file_info(dirname):
    output = []
    files = [file for file in glob.glob(dirname + '\\*') if path.isfile(file)]
    for file in files:
        output.append({
            'file name': file.split('\\')[-1],
            'file size': stat(file).st_size,
            'last modification': stat(file).st_mtime
        })
    return json.dumps(output, indent=4)


print(write_file_info('ch05-files'))