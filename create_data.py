'''Functions For Getting And Creating Usable Data'''
import urllib.request

def get_data(url):
    '''get_data fetches data from a site

    :URL: The url to scrape
    :return: list of page source seperated by line
    '''

    with urllib.request.urlopen(url) as file:
        text = file.read()
    return text.decode("utf-8").split('\n')


def create_lists(lines, mask_string, my_list=None):
    '''create_lists creates a list for the wanted value, ex: name, price

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
                 ';', 'gtm_categories', '\r', '=', "\\", mask]
        for word in words:
            if word in string:
                my_list[i] = my_list[i].replace(word, '').strip()
    return my_list


def arr_to_int(my_list):
    '''arr_to_int makes all elements in list a float

    :my_list: list to fix
    :return: fixed list
    '''
    for i, string in enumerate(my_list):
        my_list[i] = float(string)
    return my_list
