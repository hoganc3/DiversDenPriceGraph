import urllib.request
import createList as cl

url = 'https://www.liveaquaria.com/divers-den/category/3/marine-fish'
r = urllib.request.urlopen(url)
text = r.read()

lines = text.decode("utf-8").split('\n')
names = cl.createLists(lines,"name")
price = cl.createLists(lines,"price")


for i in range(len(price)):
    print(names[i])
    print(price[i])
