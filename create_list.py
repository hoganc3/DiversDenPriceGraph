'''Create Array Functions'''


def create_arrays(lines, mask_string, my_array=None):
    '''create_arrays creates a array for the wanted value, ex:(name, price)

    :lines: array of source code by line
    :str: used to mask data from source code
    :array=None: initialize array
    :return: array of wanted values
    '''
    if my_array is None:
        my_array = []
    mask = (f'["{mask_string}"]')
    for string in lines:
        if mask in string:
            my_array.append(string)
        else:
            pass
    fix_string(my_array)
    return my_array


def fix_string(my_array):
    '''fix_string removed unwanted characters from string

    :array: array to be fixed
    :return: array with fixed strings
    '''
    for i, string in enumerate(my_array):
        mask = (f'[{i}]')
        words = ['["price"]', '["name"]', '"',
                 ';', 'gtm_categories', '\r', '=', mask]
        for word in words:
            if word in string:
                my_array[i] = my_array[i].replace(word, '').strip()
    return my_array

def arr_to_int(my_array):
    for i, string in enumerate(my_array):
        my_array[i] = float(string)
    return my_array
