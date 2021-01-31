# import requests

# response = requests.get('https://gist.githubusercontent.com/reuven/7647d1af56cc8c6a9744/raw/4a0968a11a0a30e34466030a203b5f91493beac5/passwd.txt')
# response.raise_for_status()

# with open('ch05-files\\pswd.txt', 'wb') as f:
#     f.write(response.content)


def passwd_to_dict(filename):
    users = {}

    with open(filename) as f:
        for line in f:
            if not line.startswith(('\n', '#')):
                line = line.split(':')
                user = line[0]
                user_id = line[2]
                if user not in users:
                    users[user] = int(user_id)
    return users


def shells_users(filename):
    shells = {}

    with open(filename) as logs:
        for log in logs:
            if not log.startswith(('\n', '#')):
                log = log.strip().split(':')
                shells.setdefault(log[-1], []).append(log[0])
    return shells


# print(shells_users('ch05-files\\pswd.txt'))


def factor(n):
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k*k == n:
        yield k

def calculate_factors(numbers):
    factors = {}
    numbers = list(map(int, numbers.split()))
    for n in numbers:
        if n not in factors:
            factors[n] = sorted(factor(n))
    return factors


# print(calculate_factors('1 2 3 4 5 6 7 8 9 10'))

def users_info(filename):
    users = {}
    with open(filename) as logs:
        for log in logs:
            if not log.startswith(('#', '\n')):
                log = log.strip().split(':')
                if log[0] not in users:
                    users[log[0]] = {
                        'id': log[2],
                        'home dir': log[-2],
                        'shell': log[-1]
                    }
    return users

print(users_info('ch05-files\\pswd.txt'))

# From /etc/passwd, create a dict in which the keys are the usernames
# (as in the main exercise) and the values are themselves dicts with keys
# (and appropriate values) for user ID, home directory, and shell.