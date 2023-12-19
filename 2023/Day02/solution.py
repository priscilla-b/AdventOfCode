"""
Date: 01/12/2023

Solving https://adventofcode.com/2023/day/1

Using template from https://aoc.just2good.co.uk/python/my-aoc-template

Problem:
    Given a document with a list of text. Find the sum of all calibration
    values in the document. A calibration value can be derived from each line of text
    by forming a two digit number with the first and last digit(in that order) in the text.

Solution Overview:
Part 1:
    In solution 1, the idea is to iterate through all the characters in each line and 
    check if they're digits, then get the first and last digits.
    A digit list was created and a character was marked as a digit if they're present in the digit list

    There are two ways to get the first and last digits:
        1. create a list of all digits and use list indexes 0 and -1
        to get the first and list digits respectively. Illustrated in the
        part_one_with_list() function
        
        2. avoid storing a list of digits by creating two variables to store the first
        and last digits. Both variables are initialized as None. Check if a character is a digit
        and then set it as the first digit if the first digit is still None. If a first digit has been 
        assigned, then assign it as the last digit. This process is repeated for all character in a given
        line of text. At the end of the iteration, check if the last digit is still None and set its value
        to that of the first digit. This accounts for when a text contains only one digit

"""

from pathlib import Path
import time
from Common.common import get_logger

log = get_logger()

SCRIPT_DIR = Path(__file__).parent

INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

DIGITS = [str(i) for i in range(10)]

DIGITS_DICT = {
    'one':'1',
    'three':'3',
    'two':'2',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
    }


def main():
    

    def part_one_with_list():
        sum_of_digits = 0

        log.info("with list")
        with open (INPUT_FILE) as f:
            input_data = f.read().splitlines()
            for text in input_data:
                input_digits = [x for x in text if x in DIGITS]

                try:
                    first = input_digits[0]
                except IndexError:
                    first = 0
                try:
                    last = input_digits[-1]
                except IndexError:
                    last = 0

               
                two_digits = int(first + last)
               

                sum_of_digits += two_digits
            
                # log.debug('%s : %s', text, two_digits)

        log.debug('sum_of_digits: %s', sum_of_digits)

    def part_one_without_list():

        log.info("without list")

        sum_of_digits = 0
        with open (INPUT_FILE) as f:
            input_data = f.read().splitlines()


        for text in input_data:
            first = None
            last = None
            for char in text:
                if char in DIGITS:
            
                    if not first:
                        first = char
                        continue

                    if first:
                        last = char
                        continue

            if first and not last:
                last = first

            try:
                    two_digits = int(first + last)
            except TypeError:
                two_digits = 0

            sum_of_digits += two_digits

            # log.debug('%s : %s', text, two_digits)

        log.debug('sum_of_digits: %s', sum_of_digits)



    def part_two():

        log.info("part two")


        sum_of_digits = 0
        with open (INPUT_FILE) as f:
            input_data = f.read().splitlines()


        for text in input_data:
            digit_text = text.lower()

            for k, v in DIGITS_DICT.items():
                digit_text =  digit_text.replace(k, k[0]+v+k[-1])
                # to account for overlapping digits when replace a 
                # digit text include the first and last digits

            first = None
            last = None
            for char in digit_text:
                if char in DIGITS:
            
                    if not first:
                        first = char
                        continue

                    if first:
                        last = char
                        continue

            if first and not last:
                last = first

            try:
                    two_digits = int(first + last)
            except TypeError:
                two_digits = 0

            sum_of_digits += two_digits

            # log.debug('%s : %s', text, two_digits)

        log.debug('sum_of_digits: %s', sum_of_digits)

    t1 = time.perf_counter()
    part_one_with_list()
    t2 = time.perf_counter()
    log.info("Execution time: %0.4f seconds", t2 - t1)
        

    t1 = time.perf_counter()
    part_one_without_list()
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



