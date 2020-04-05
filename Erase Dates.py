import os



#File Path of Script
HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, 'song_titles.txt'), 'r', encoding="utf-8") as file:
    lines = file.readlines()

with open(os.path.join(HERE, 'song_titles.txt'), "w",  encoding="utf-8") as file:
    for line in lines:
        if not line.strip("\n").isdigit():
            file.write(line)