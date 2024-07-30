from itertools import combinations
from math import factorial, sqrt

with(open('input.txt', 'r')) as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    lines[i] = [char for char in line.strip()]

def get_distance_straight(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_distance_L(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def part1(lines):
    # pretty straight forward, we need to add a row if there is no galaxy in that row
    space : list = []
    for line in lines:
        space.append(line[:])

        if "#" not in line:
            space.append(line[:])
    
    n, m = len(space), len(space[0])

    # I hesitated, I could have rotated the matrix and used the same code as above
    # but I decided to try to add manually the columns
    col_to_insert = []
    for j in range(m):      
        if "#" not in [space[i][j] for i in range(n)]:
            col_to_insert.append(j)  
    
    for it, col in enumerate(col_to_insert):
        for i in range(n):
            # col + it since we are adding columns in the matrix, it being the i-th - 1 column added 
            space[i].insert(col+it, ".")
          
    galaxies = []
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == "#":
                galaxies.append((i, j))
    
    counter_galaxies = 0
    for s in space:
        for c in s:
            if c == "#":
                counter_galaxies += 1

    # number of combinations of galaxies - n! / (2! * (n-2)!)
    number_of_combinations = int(factorial(counter_galaxies) / (factorial(2) * factorial(counter_galaxies - 2)))

    distance = []
    comb = list(combinations(galaxies, 2))
    for c in comb:
        distance.append((c[0], c[1], get_distance_L(c[0], c[1])))
    
    print('part 1:', sum(dist[2] for dist in distance))

def part2(lines):

    expension_factor = 999_999 #each empty row should be replaced with 1000000 empty rows
    space : list = []
    for line in lines:
        space.append(line[:])
    n, m = len(space), len(space[0])

    row_to_insert = []
    for i in range(n):
        if "#" not in space[i]:
            row_to_insert.append(i)

    col_to_insert = []
    for j in range(m):      
        if "#" not in [space[i][j] for i in range(n)]:
            col_to_insert.append(j)

    galaxies = []
    for i in range(n):
        for j in range(m):
            if space[i][j] == "#":
                galaxies.append((i, j))
            
    
    counter_galaxies = 0
    for s in space:
        for c in s:
            if c == "#":
                counter_galaxies += 1
    
    # number of combinations of galaxies - n! / (2! * (n-2)!)
    number_of_combinations = int(factorial(counter_galaxies) / (factorial(2) * factorial(counter_galaxies - 2)))

    distance = []
    comb = list(combinations(galaxies, 2))
    for c in comb:

        if c[0][0] > c[1][0] and c[0][1] > c[1][1]:
            c = (c[1], c[0])
        
        if c[0][0] > c[1][0]:
            c = ((c[1][0], c[0][1]), (c[0][0], c[1][1]))
        
        if c[0][1] > c[1][1]:
            c = ((c[0][0], c[1][1]), (c[1][0], c[0][1]))

        new_c1_row = (c[1][0] + expension_factor * sum(row in range(c[0][0], c[1][0]) for row in row_to_insert))
        new_c1_col = (c[1][1] + expension_factor * sum(col in range(c[0][1], c[1][1]) for col in col_to_insert))
        distance.append((c[0], c[1], get_distance_L(c[0], (new_c1_row, new_c1_col))))

    print('part 2:', sum(dist[2] for dist in distance))


def main():
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()