import os
import time
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
# START_YEAR = 1946

# while START_YEAR <=2019 :
with open(str(os.path.join(HERE, 'test.html')), encoding="utf8") as html_file:
    SOUP = BeautifulSoup(html_file, 'lxml')

    HTML_TEXT = SOUP.find_all('td')


COUNTER = 0
for td in SOUP.find_all("td"):
    line = td.text
    if not line[0].isdigit() and line[0] == "\"":
        COUNTER += 1
        SONG_LIST.append(str(COUNTER) + ": " + line)
    elif not line[0].isdigit():
        SONG_LIST.append("    " + line)


with open(os.path.join(HERE, 'song_titles.txt'), 'w') as file:
    for string in SONG_LIST:
        file.write(string + "\n")
