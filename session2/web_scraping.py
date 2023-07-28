# https://de.wikipedia.org/wiki/Steven_Spielberg

# pip install beautifulsoup4
# pip install lxml
# pip install requests

import requests
from bs4 import BeautifulSoup
import csv

links = ["https://de.wikipedia.org/wiki/Steven_Spielberg", "https://de.wikipedia.org/wiki/John_Travolta"]

for l in links:
    source = requests.get(l).text

    site = BeautifulSoup(source, "lxml")

    # print(site.prettify())

    seiten_titel = site.find("h1").text

    # print(seiten_titel)

    rubriken = site.find_all("span", class_="mw-headline")

    for r in rubriken:
        # print(r.text)
        print("-----------------------")

    ################ Alles Filme mit Regie als CSV speichern #####################

    table = site.find("div", class_="column-multiple")

    filename = seiten_titel.replace(" ", "_") + "_movies.csv"

    # print(table.prettify())

    movies = table.find_all("li")

    movies_file = open(filename, "w")

    file_writer = csv.writer(movies_file)

    file_writer.writerow(["Jahr", "Titel"])

    for m in movies:
        # print(m.text)
        print("---------------------------")

        # year = m.text.split(":")[0]

        year = m.text[:4]

        print(year)

        title = m.text[6:]

        print(title)

        file_writer.writerow([year, title])

    movies_file.close()



