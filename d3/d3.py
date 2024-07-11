import numpy as np
import re
from operator import mul

list_not_symbol = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


# part 1
list_to_sum = np.array([])

mask = np.array([[]])
adjacent = np.array([])

size = 0
length = 0

# Read all lines from the file and store them in a list
with open('input.txt') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
size = len(lines)
length = max(len(line) for line in lines)

mask = np.zeros((size, length), dtype=str) 
adjacent = np.zeros((size, length))

# Fill the mask array with the lines from the file
for i, line in enumerate(lines):
    for j in range(len(line)):
        mask[i][j] = line[j]

for i in range(len(mask)):
    for j in range(len(mask[0])):

        if mask[i][j] not in list_not_symbol:
            
            #check if around TOP is possible:
            if ((i - 1) and (j-1)) >= 0:
                adjacent[i-1][j-1] = 1
            
            if (i - 1) >= 0:
                adjacent[i-1][j] = 1
            
            if (i - 1 >= 0) and (j+1 < len(mask[0])):
                adjacent[i-1][j+1] = 1
            
            #check if around MIDDLE is possible:
            if (j-1) >= 0:
                adjacent[i][j-1] = 1

            if (j+1) < len(mask[0]):
                adjacent[i][j+1] = 1
            
            #check if around BOTTOM is possible:
            if (i+1 < len(mask)) and (j-1 >= 0):
                adjacent[i+1][j-1] = 1
            
            if (i+1) < len(mask):
                adjacent[i+1][j] = 1
            
            if (i+1 < len(mask)) and (j+1 < len(mask[0])):
                adjacent[i+1][j+1] = 1

        
# extend the adjacent array to the left and right for numbers
for i in range(len(mask)):
    for j in range(len(mask[0])):

        itera = 1
        while True:
            if adjacent[i][j] == 1 and (j-itera) >= 0 and mask[i][j-itera] in number and mask[i][j] in number:
                adjacent[i][j-itera] = 1
                itera += 1
            else:
                break
        
        itera = 1
        while True:
            if adjacent[i][j] == 1 and (j+itera) < len(mask[0]) and mask[i][j+itera] in number and mask[i][j] in number:
                adjacent[i][j+itera] = 1
                itera += 1
            else:
                break

number_to_add = ''
for i in range(len(mask)):
    for j in range(len(mask[0])):
        if adjacent[i][j] == 1 and mask[i][j] in number:
            number_to_add = number_to_add + mask[i][j]
        
        if adjacent[i][j] == 0 and number_to_add != '':
            list_to_sum = np.append(list_to_sum, int(number_to_add))
            number_to_add = ''
        
        if mask[i][j] not in number and number_to_add != '':
            list_to_sum = np.append(list_to_sum, int(number_to_add))
            number_to_add = ''

        if j == len(mask[0]) - 1 and number_to_add != '':
            list_to_sum = np.append(list_to_sum, int(number_to_add))
            number_to_add = ''
        

print(f"Part 1: {int(np.sum(list_to_sum))}")
            

# part 2


gear_regex = r'\*'
gears = dict()
for i, line in enumerate(lines):
    for m in re.finditer(gear_regex, line):
        gears[(i, m.start())] = [] # Find the position of gear and store it in a dictionary

print(gears)

number_regex = r'\d+'
for i, line in enumerate(lines): # Iterate through the lines
    for m in re.finditer(number_regex, line): # Find the numbers in the line
        for r in range(i-1, i+2): # Check the rows above and below the number
            for c in range(m.start()-1, m.end()+1): # Check the columns before and after the number
                if (r, c) in gears: # If the position tuple is a gear
                    gears[(r, c)].append(int(m.group())) # Add the number by group to the gear

gear_ratio_sum = 0
for nums in gears.values(): # Iterate through the values of the gears
    if len(nums) == 2: # If we have 2 numbers wich means 2 numbers are connected to the gear
        gear_ratio_sum += mul(*nums)

print(f"Part 2: {gear_ratio_sum}")


# with the help of : https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_03.py
# For regex expression...
