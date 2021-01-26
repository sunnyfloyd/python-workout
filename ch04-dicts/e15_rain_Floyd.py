def get_rainfall():
    cities_rainfall = dict()
    while True:
        city = input('Enter city name:')
        if not city:
            break
        rainfall = int(input())
        cities_rainfall[city] = rainfall + cities_rainfall.get(city, 0)

    for city, rainfall in cities_rainfall.items():
        print(f'{city}: {rainfall}')


def get_avg_rainfall():
    cities_rainfall = dict()
    while True:
        city = input('Enter city name:')
        if not city:
            break
        rainfall = int(input())
        cities_rainfall[city] = [rainfall + cities_rainfall.get(city, [0, 0])[0],
                                 cities_rainfall.get(city, [0, 0])[1] + 1]

    for city, rainfall in cities_rainfall.items():
        print(f'{city}: total: {rainfall[0]} avg: {rainfall[0]/rainfall[1]}')


from collections import Counter


def word_len_count():
    with open('C:\\Users\\mdebs\\Documents\\GitHub\\python-workout\\ch04-dicts\\wazne.txt') as file:
        content = ''.join(file.readlines()).split()
        words_len = [len(word) for word in content]
        print(Counter(words_len).most_common(1))
    

word_len_count()
