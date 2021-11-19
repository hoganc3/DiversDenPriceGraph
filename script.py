import urllib.request

url = 'https://www.liveaquaria.com/divers-den/category/3/marine-fish'
r = urllib.request.urlopen(url)

text = r.read()

lines = text.decode("utf-8").split('\n')
names = []
price = []


def createLists(lines):
    for x in lines:
        if '["price"]' in x:
            price.append(x.translate(
                {ord(i): None for i in 'gtm_categories[]""price;'}))
        elif '["name"]' in x:
            names.append(x)
        else:
            pass


createLists(lines)

for x in price:
    print(f"{x}\n")
