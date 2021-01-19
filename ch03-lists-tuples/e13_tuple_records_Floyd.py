import operator
from collections import namedtuple

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(people):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    people = sorted(people, key=operator.itemgetter(1))

    for person in people:
        output.append(template.format(*person))
    return output

MOVIES = [  ('ABC', 200, 'Schwarzi'),
            ('Przeminelo', 120, 'Irish Dude'),
            ('Gantusta', 190, 'Zanussi'),
            ('ABC', 190, 'Zdenek')]

def sort_movies(movies):
    sorts = {'name': 0, 'length': 1, 'director': 2}
    user_input = input('How do you want to sort: ').lower().split(',')
    sort_type = (sorts[x.strip()] for x in user_input if x.strip() in sorts.keys())
    return sorted(movies, key=operator.itemgetter(*sort_type))

print(sort_movies(MOVIES))