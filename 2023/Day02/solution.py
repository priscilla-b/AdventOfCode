"""
Date: 01/12/2023

Solving https://adventofcode.com/2023/day/1

Using template from https://aoc.just2good.co.uk/python/my-aoc-template

Problem:
    Given a document with a list of text where each line of text represent a game played, find the sum
    of all possible games. A game consists of a combination of red, blue and green cubes

Solution Overview:
Part 1:

Part 2:


"""

from pathlib import Path
import time
import re
from Common.common import get_logger

log = get_logger()

SCRIPT_DIR = Path(__file__).parent

INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

cubes_dict = {
    "blue":14,
    "green":13,
    "red":12
}

allowed_colors = set(cubes_dict.keys())



def main():
    

    def part_one():
        
        with open (INPUT_FILE) as f:
            input_data = f.read().splitlines()

        total_games = 0
        sum_impossible_games = 0

        for text in input_data:
    
            split_pattern = r'[:;,]'
            text_contents = re.split(split_pattern, text)

            game_id = int(text_contents[0].split(' ')[1])
            
            total_games += game_id

            picks = text_contents[1:]

            for pick in picks:
                pick_info = pick.strip().split(' ')

                if len(pick_info) != 2:
                    print(f"Error in input format in Game {game_id}")
                    continue

                value = int(pick_info[0])
                color = pick_info[1].lower()


                if color not in allowed_colors or value > cubes_dict[color]:
                    sum_impossible_games += game_id
                    break
            
    
        sum_possible_games  = total_games - sum_impossible_games
        log.debug('sum possible games: %s', sum_possible_games)




    def part_two():

        log.info("part two")


        

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    log.info("Execution time: %0.4f seconds", t2 - t1)
        

 

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    log.info("Execution time: %0.4f seconds", t2 - t1)


if __name__ == "__main__":
    # t1 = time.perf_counter()
    main()
    # t2 = time.perf_counter()
    # log.info("Execution time: %0.4f seconds", t2 - t1)



