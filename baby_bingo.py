
########## SUPPORTING PACKAGES ##########
import random
import re
import sys


########## SUPPORTING FUNCTIONS ##########

def remove_number_prefix(my_string):
    m = re.match('^[0-9]*[.]\s(.*)', my_string)
    return(m.group(1))

def remove_rating_suffix(my_string):
    m = re.match('([a-zA-Z]*)\s(No change)*[+-]*[0-9]*', my_string)
    return m.group(1)


########## CODE TO BE EXECUTED ##########

baby_names = [] # array that will store the baby names
bingo_card_dim = 4 # the number of rows and columns the bingo card will include
num_cards_needed = 15 # the number of bingo cards needed

# open, read in, and close the file
in_file = open('baby_names.txt', 'r')

for line in in_file:

    # clear away the extraneous prefix / suffix strings
    current_line = remove_rating_suffix(remove_number_prefix(str(line)))

    # store it in a list
    baby_names.append(current_line)

in_file.close()


# open a file to write to, loop through and print the number of needed bingo cards, and close the file

sys.stdout = open('bingo_cards.csv', 'w')

for i in range(0, num_cards_needed):
    for j in range(0, bingo_card_dim):
        for k in range(0, bingo_card_dim):

            # print (w/o a newline) a random baby name
            sys.stdout.write(baby_names[random.randint(0, len(baby_names) - 1)]),

            # print a comma to separate the names unless it's the final one of the row
            if (k < bingo_card_dim - 1):
                sys.stdout.write(", ")

        # print a newline to move to the next row
        sys.stdout.write("\n")

    # print a newline to separate this bingo card from the next
    sys.stdout.write("\n")

sys.stdout.close()

# temp change to create review
