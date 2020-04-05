import os
import time
import random
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
    time.sleep(random.randint(5, 10))
    URL_ID = "https://en.wikipedia.org/wiki/Billboard_year-end_top_singles_of_"
    SOUP = BeautifulSoup(URL_ID + str(START_YEAR), 'lxml')
    HTML_TEXT = SOUP.find_all('td')

    SONG_LIST.append("Billboards Top Selling Songs For The Year: " + str(START_YEAR))
    print("Current Year = " + str(START_YEAR))

    COUNTER = 0
    for td in SOUP.find_all("td"):
        line = td.text
        if not line[0].isdigit() and line[0] == "\"":
            COUNTER += 1
            SONG_LIST.append(str(COUNTER) + ": " + line)
        elif not line[0].isdigit():
            SONG_LIST.append("    " + line)
    for i in range(2):
        SONG_LIST.append("")
    START_YEAR += 1


with open(os.path.join(HERE, 'song_titles.txt'), 'a') as file:
    for string in SONG_LIST:
        file.write(string + "\n")
