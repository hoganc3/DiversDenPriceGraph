def create_lists(lines, str, ls=None):
    '''create_lists creates a list for the wanted value, ex:(name, price)

    :lines: list of source code by line
    :str: used to mask data from source code
    :ls=None: initialize list
    :return: list of wanted values
    '''
    if ls is None:
        ls = []
    mask = (f'["{str}"]')
    for str in lines:
        if mask in str:
            ls.append(str)
        else:
            pass
    fix_string(ls)
    return ls


def fix_string(ls):
    '''fix_string removed unwanted characters from string

    :ls: list to be fixed
    :return: list with fixed strings
    '''
    for i, str in enumerate(ls):
        s = (f'[{i}]  ')
        words = ['["price"]', '["name"]', '"',
                 ';', 'gtm_categories', '\r', '=', s, ]
        for word in words:
            ls[i] = ls[i].replace(word, '')
    return ls
