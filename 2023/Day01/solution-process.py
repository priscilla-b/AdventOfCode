import os
from pathlib import Path


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

INPUT_PATH = Path(SCRIPT_DIR, 'input/input.txt')
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

sum_of_digits = 0
# solution one
# with open (INPUT_PATH) as f:
#     input_data = f.read().splitlines()
#     for text in input_data:
#         input_digits = [x for x in text if x in DIGITS]

#         first = input_digits[0]
#         last = input_digits[-1]

#         two_digits = int(first + last)

#         sum_of_digits += two_digits

#         print(text, ':', two_digits)
#         print('sum_of_digits: ', sum_of_digits)

# solution two
# with open (INPUT_PATH) as f:
#     input_data = f.read().splitlines()

#     for text in input_data:
#         first = None
#         last = None
#         for char in text:
#             if char in DIGITS:
           
#                 if not first:
#                     first = char
#                     continue

#                 if first:
#                     last = char
#                     continue

#         if first and not last:
#             last = first

#         try:
#             two_digits = int(first + last)
#         except TypeError:
#             two_digits = 0

#         sum_of_digits += two_digits

#         print(text, ':', two_digits)
#     print('sum_of_digits: ', sum_of_digits)


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


with open (INPUT_PATH) as f:
    input_data = f.read().splitlines()

    
    for text in input_data:
        digit_text = text.lower()
        for k, v in DIGITS_DICT.items():
            digit_text =  digit_text.replace(k, v)

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

        print(text, ':', two_digits)
    print('sum_of_digits: ', sum_of_digits)


     


                
        
    
