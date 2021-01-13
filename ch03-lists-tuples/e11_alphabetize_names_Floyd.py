PEOPLE = [{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'}
 ]

def alphabetize_names(dicts):
    return sorted(dicts, key=lambda x: f"{x['last']} {x['first']}")

def sort_absolute(numbers):
    return sorted(numbers, key=abs)

def sort_by_vowel_count(strings):
    vowels = 'aeiouy'
    return sorted(strings, key=lambda x: sum(1 for y in x.lower() if y in vowels), reverse=True)

def sort_by_sum(list_of_nums):
    return sorted(list_of_nums, key=sum)


n = sort_by_sum([[1,2,3], [1], [1,2,3,4], [0,1], [], [4,0]])

print(n)