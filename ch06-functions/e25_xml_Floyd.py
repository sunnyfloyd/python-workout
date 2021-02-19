def myxml(tag, content='', **attributes):
    tag_with_attributes = [tag] + [f'{k}="{v}"' for k,v in attributes.items()]
    return f"<{' '.join(tag_with_attributes)}>{content}</{tag}>"


# print(myxml('lol','nothing', a='a', b='b', c=1))


def copyfile(input_filename, *args):
    with open(input_filename) as input_file:
        content = input_file.readlines()
    for output_filename in args:
        with open(output_filename, 'w') as output_file:
            output_file.writelines(content)


# copyfile(
#     'ch06-functions\copy_pasta.txt',
#     'ch06-functions\copy_1.txt',
#     'ch06-functions\copy_2.txt'
# )


def factorialish(*args):
    output = 1
    for i in args:
        if isinstance(i, (int, float)):
            output *= i
    return output if args else None


# print(factorialish(3.0, 4.4))

def anyjoin(sequence, glue=' '):
    return glue.join(f'{char}' for char in sequence)
    # output = str(sequence[0])
    # for char in sequence[1:]:
    #     output += f'{glue}{char}'
    # return output


print(anyjoin([1,2,3], '*^'))