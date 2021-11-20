'''Runs program'''

import urllib.request
import create_list as cl

URL = 'https://www.liveaquaria.com/divers-den/category/3/marine-fish'
with urllib.request.urlopen(URL) as r:
    text = r.read()

lines = text.decode("utf-8").split('\n')
names = cl.create_lists(lines,"name")
price = cl.create_lists(lines,"price")


for i, x in enumerate(price):
    print(names[i])
    print(price[i])
