'''Create List Functions'''


def create_lists(lines, mask_string, my_list=None):
    '''create_lists creates a list for the wanted value, ex:(name, price)

    :lines: list of source code by line
    :str: used to mask data from source code
    :list=None: initialize list
    :return: list of wanted values
    '''
    if my_list is None:
        my_list = []
    mask = (f'["{mask_string}"]')
    for string in lines:
        if mask in string:
            my_list.append(string)
        else:
            pass
    fix_string(my_list)
    return my_list


def fix_string(my_list):
    '''fix_string removed unwanted characters from string

    :list: list to be fixed
    :return: list with fixed strings
    '''
    for i, string in enumerate(my_list):
        mask = (f'[{i}]')
        words = ['["price"]', '["name"]', '"',
                 ';', 'gtm_categories', '\r', '=', mask]
        for word in words:
            if word in string:
                my_list[i] = my_list[i].replace(word, '').strip()
    return my_list
