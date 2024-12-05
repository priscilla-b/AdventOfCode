import os
from pathlib import Path
import re



SCRIPT_DIR = Path(__file__).parent  # get the directory program is running from

INPUT_PATH = Path(SCRIPT_DIR, 'input/input.txt')

# cubes_dict = {
#     "blue":14,
#     "green":13,
#     "red":12
# }

# allowed_colors = set(cubes_dict.keys())


# with open (INPUT_PATH) as f:
#     input_data = f.read().splitlines()

# total_games = 0
# sum_impossible_games = 0

# for text in input_data:
    
#     split_pattern = r'[:;,]'
#     text_contents = re.split(split_pattern, text)

#     game_id = int(text_contents[0].split(' ')[1])
    
#     total_games += game_id

#     picks = text_contents[1:]

#     for pick in picks:
#         pick_info = pick.strip().split(' ')

#         if len(pick_info) != 2:
#             print(f"Error in input format in Game {game_id}")
#             continue

#         value = int(pick_info[0])
#         color = pick_info[1].lower()


#         if color not in allowed_colors or value > cubes_dict[color]:
#             sum_impossible_games += game_id
#             break
        
    
# sum_possible_games  = total_games - sum_impossible_games
    

# print("sum possible games: ", sum_possible_games)
    


# part two: fewest number of cubes needed in the bag at a time to make a game possible



with open (INPUT_PATH) as f:
    input_data = f.read().splitlines()

sum_power_set = 0



for text in input_data:
    split_pattern = r'[:;,]'
    text_contents = re.split(split_pattern, text)

    picks = text_contents[1:]

    power_set = 1

    cubes_dict = {
        "blue":0,
        "green":0,
        "red":0
    }

    for pick in picks:
        pick_info = pick.strip().split(' ')

       
        value = int(pick_info[0])
        color = pick_info[1].lower()

        try:
            color_value = cubes_dict[color]

            if value > color_value:
                cubes_dict[color] = value

        except(KeyError):
            print("color does not exist in cube dictionary")
            continue

        

    for value in cubes_dict.values():
        power_set *= value

    sum_power_set += power_set
    
        
        

print("sum power set: ", sum_power_set)
    





    


            
    

