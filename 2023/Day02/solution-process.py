import os
from pathlib import Path
import re


# f = open('input/sample-input.txt', mode="rt")

# 'r' means read. 't' means text.
# 'rt' means open for reading text. default mode, so not necessary to specify
#  modes are important because it prevents your program from making unexpected
#  changes to your program. E.g. your program modifying a file you only intended to read
# input_data = f.read().splitlines()
# for line in input_data:
#     pass
#     # print(line)
# f.close()

# using Pathlib to read file paths ensures your program is agnostic of 
# operating systems
SCRIPT_DIR = Path(__file__).parent  # get the directory program is running from

INPUT_PATH = Path(SCRIPT_DIR, 'input/sample-input.txt')

{
    "blue":12,
    "green":13,
    "blue":14
}


with open (INPUT_PATH) as f:
    input_data = f.read().splitlines()

    sum_possible_games = 0
    for text in input_data:
        split_pattern = r'[:;,]'
        text_contents = re.split(split_pattern, text)
        # text_contents = text.split(":");
        # game_num = text_contents[0][-1]
        # games = text_contents[1].split(";")
        # for game in games: 
        #     print("game ", game_num, game)

        print(text_contents[0][-1], text_contents[1:])
    


     


                
        
    
