import os
import time
import random
import requests
from bs4 import BeautifulSoup



#File Path of Script
HERE = os.path.dirname(os.path.abspath(__file__))

#try making a new text file to store song names
try:
    with open(os.path.join(HERE, 'song_titles.txt'), 'x') as file:
        pass

except FileExistsError:
    pass

SONG_LIST = []
START_YEAR = 1946

while START_YEAR <= 2019:
    SONG_LIST.append("The Year Is: " + str(START_YEAR))
    if START_YEAR <= 1948:
        URL_ID = "https://en.wikipedia.org/wiki/Billboard_year-end_top_singles_of_"
    if 1949 <= START_YEAR <= 1955:
        URL_ID = "https://en.wikipedia.org/wiki/Billboard_year-end_top_30_singles_of_"
    if 1956 <= START_YEAR <= 1958:
        URL_ID = "https://en.wikipedia.org/wiki/Billboard_year-end_top_50_singles_of_"
    if START_YEAR >= 1959:
        URL_ID = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"

    SOURCE = requests.get(URL_ID + str(START_YEAR)).text
    SOUP = BeautifulSoup(SOURCE, 'lxml')
    HTML_TEXT = SOUP.find_all('td')

    # SONG_LIST.append("Billboards Top Selling Songs For The Year: " + str(START_YEAR))
    print("Current Year = " + str(START_YEAR))

    COUNTER = 0
    for td in SOUP.findAll("table", {"class": "wikitable sortable"}):
        line = td.text
        if len(line) >= 1:
            if not line.isdigit() and line[0] == "\"":
                COUNTER += 1
                SONG_LIST.append(line)
            elif not line.isdigit():
                COUNTER += 1
                SONG_LIST.append(line)

    time.sleep(3)
    START_YEAR += 1



with open(os.path.join(HERE, 'song_titles.txt'), 'w', encoding="utf-8") as file:
    for string in SONG_LIST:
        file.write(string)

with open(os.path.join(HERE, 'song_titles.txt'), 'r', encoding="utf-8") as file:
    LINES = file.readlines()

with open(os.path.join(HERE, 'song_titles.txt'), "w", encoding="utf-8") as file:
    for line in LINES:
        if line in ['\n', '\r\n']:
            pass
        elif line.strip("\n") in ["Position", "Song", "Artist"]:
            pass
        elif line.strip("\n").isdigit():
            pass
        else:
            file.write(line)
