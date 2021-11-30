'''Runs program'''
import pandas as pd
import matplotlib.pyplot as plt
import create_data as cd


def prompt():
    '''Prompts the user what information they want to see.

    :returns: page URL
    '''
    page_list = {
        "Marine Fish": "https://www.liveaquaria.com/divers-den/category/3/marine-fish",
        "Freshwater": "https://www.liveaquaria.com/divers-den/category/11/freshwater",
        "Betta Fish": "https://www.liveaquaria.com/divers-den/category/12/betta-fish",
        "Inverts": "https://www.liveaquaria.com/divers-den/category/4/inverts",
        "Maricultured Corals":
            "https://www.liveaquaria.com/divers-den/category/6/maricultured-corals",
        "Aquacultured Corals":
            "https://www.liveaquaria.com/divers-den/category/5/aquacultured-corals",
        "Soft Corals":
            "https://www.liveaquaria.com/divers-den/category/7/polyp-mushroom-and-soft-corals",
        "LPS Corals": "https://www.liveaquaria.com/divers-den/category/8/lps-corals",
        "SPS Corals": "https://www.liveaquaria.com/divers-den/category/2/sps-corals",
        "NPS Corals": "https://www.liveaquaria.com/divers-den/category/10/non-photosynthetic-nps",
        "Deals": "https://www.liveaquaria.com/divers-den/category/9/deals-steals"
    }
    print("""Welcome to the LiveAquaria Scraper!
    What information would you like to know about?
    Please pick one from the following
    \t- Marine Fish
    \t- Freshwater
    \t- Betta Fish
    \t- Inverts
    \t- Maricultured Corals
    \t- Aquacultured Corals
    \t- Soft Corals
    \t- LPS Corals
    \t- SPS Corals
    \t- NPS Corals
    \t- Deals
    """)

    not_answered = True
    while not_answered:
        answer = input("> ")
        if answer in page_list:
            return page_list[answer]


def display_data(names, price):
    '''Creates and displays data graph

    :names: List of item name
    :price: Price of item
    '''
    data = {
        'Name': names,
        'Price': price
    }

    data_frame = pd.DataFrame(data, columns=['Name', 'Price'])
    data_frame = data_frame.sort_values(by="Price")
    data_frame["Number"] = list(range(0, len(names)))
    data_frame = data_frame.set_index('Number')
    print(data_frame.to_string())

    data_frame.plot(kind='scatter', x="Name", y="Price")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.subplots_adjust(top=.98, left=.05, right=.98)
    plt.show()


def main():
    '''main runs the program'''

    url = prompt()
    lines = cd.get_data(url)
    names = cd.create_lists(lines, "name")
    price = cd.create_lists(lines, "price")
    price = cd.arr_to_int(price)
    display_data(names, price)


if __name__ == '__main__':
    main()
