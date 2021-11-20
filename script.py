import urllib.request


def createLists(lines):
    for str in lines:
        if '["price"]' in str:
            price.append(str)
        elif '["name"]' in str:
            names.append(str)
        else:
            pass


def fixString(arr):
    for i, str in enumerate(arr):
        s = (f'[{i}]')
        words = ['["price"]', '["name"]', '"', ';', 'gtm_categories','\r','=', s,' ']
        for word in words:
            str = str.replace(word, '')
        return str


url = 'https://www.liveaquaria.com/divers-den/category/3/marine-fish'
r = urllib.request.urlopen(url)

text = r.read()

lines = text.decode("utf-8").split('\n')
names = []
price = []


createLists(lines)
fixString(price)
for x in price:
    print(f"{x}")
