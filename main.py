'''Runs program'''

import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import create_list as cl

URL = 'https://www.liveaquaria.com/divers-den/category/3/marine-fish'
with urllib.request.urlopen(URL) as r:
    text = r.read()

lines = text.decode("utf-8").split('\n')
names = cl.create_arrays(lines, "name")
price = cl.create_arrays(lines, "price")
price = cl.arr_to_int(price)

for i, x in enumerate(price):
    print(names[i])
    print(price[i])

data = {
        'Fish Name': names,
        'Price': price
        }

df = pd.DataFrame(data, columns=['Fish Name', 'Price'])
df = df.sort_values(by="Price")
df["Number"] = list(range(0, len(names)))
df = df.set_index('Number')
print(df)
df.plot(kind='scatter',x="Fish Name",y="Price");
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
