def mysum(*args):
    if not args:
        return tuple()
    
    result = args[0]
    for i in range(1, len(args)):
        try:
            result += args[i]
        except:
            return
    return result

def mysum_bigger_than(limit, *args):
    if not args:
        return tuple()
    
    result = args[0]
    for arg in args[1:]:
        if arg > limit: result += arg
    return result

def sum_numeric(*args):
    result = 0
    for arg in args:
        try:
            result += int(arg)
        except:
            pass
    return result

def combine_dict(dicts):
    output_dict = {}
    for dict_ in dicts:
        for k, v in dict_.items():
            try:
                output_dict[k].append(v)
            except AttributeError:
                output_dict[k] = [output_dict[k], v]
            except KeyError:
                output_dict[k] = v
            # if k in output_dict:
            #     if type(output_dict[k]) == list:
            #         output_dict[k].append(v)
            #     else:
            #         output_dict[k] = [output_dict[k], v]
            # else:
            #     output_dict[k] = v
    return output_dict

d1 = {'a': 2, 'b': 5, 'c': 12}
d2 = {'b': 3, 'd': 7, 'g': 0, 'c': 3}
d3 = {'b': 4, 'd': 4, 'c': 4}

a = combine_dict([d1, d2, d3])

print(a)