import urllib.request

url = 'https://www.liveaquaria.com/divers-den/category/3/marine-fish'


r = urllib.request.urlopen(url)

text = r.read()

lines = text.decode("utf-8").split('\n')
names = []
price = []

createLists(lines)


def createLists(lines):
    for x in lines:
        match x:
            case '["price"]' in lines:
                names.append(x)
            case '["name"]' in lines:
                price.append(x)


for x in price:
    print("{names}\n")
