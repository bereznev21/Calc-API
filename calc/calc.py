from api.work_with_db import add_note
from calc import ARG_NAMES


def do_operation(index, items, variables):
    op = items[index]
    a = int(items[index - 1])
    b = int(items[index + 1])
    res = 0
    if op == '-':
        res = a - b
    elif op == '+':
        res = a + b
    elif op == '*':
        res = a * b
    items.pop(index-1)
    items.pop(index-1)
    items.pop(index-1)
    items.insert(index - 1, str(res))
    return items


def get_set(string):
    result = []
    index = 0
    while index < len(string):
        num = ''
        name = ''
        if string[index] in ARG_NAMES:
            while index < len(string) and string[index] in ARG_NAMES:
                name += string[index]
                index += 1
            result.append(name)
        elif string[index].isnumeric():
            while index < len(string) and string[index].isnumeric():
                num += string[index]
                index += 1
            result.append(num)
        elif string[index] in set('*-+'):
            result.append(string[index])
            index += 1
        else:
            index += 1
    return result


def calculator(args):
    variables = args['variables']
    expression = args['expression']
    items = get_set(expression)
    for index in range(len(items)):
        if variables.get(items[index]):
            items[index] = variables.get(items[index])
    while '*' in items:
        index = items.index('*')
        items = do_operation(index, items, variables)
    index = 0
    while index < len(items) and len(items) > 0:
        if items[index] in set('+-'):
            items = do_operation(index, items, variables)
            index = 0
        index += 1
    # print(items)
    id_expr = add_note(items[0])
    return id_expr
