import numpy as np

possible = {"blue": 14, "green": 13, "red": 12}
list_sum = np.array([])
list_not_possible = np.array([])

list_max = np.array([])


with open("input.txt") as file:
    for line in file:
        cubes = []
        line = line.strip("Game")
        subsets = line.strip().split(":")

        id = subsets[0]
        list_sum = np.append(list_sum, int(id))
        rest = subsets[1]
        subset = rest.split(";")

        temp = []

        for sub in subset:
            sub = sub.strip().split(",")
            temp.append(sub)

        cubes = temp

        for i, cube in enumerate(cubes):
            for j, c in enumerate(cube):
                check = c.strip().split(" ")
                if check[1] in possible:
                    if int(check[0]) > possible[check[1]]:
                        list_not_possible = np.append(list_not_possible, int(id))
                        break

list_not_possible = np.unique(list_not_possible)
list_sum = list_sum[~np.in1d(list_sum, list_not_possible)]

print(f"Part 1: {int(np.sum(list_sum))}")


# part 2
with open("input.txt") as file:
    for line in file:
        cubes = []
        line = line.strip("Game")
        subsets = line.strip().split(":")

        id = subsets[0]
        list_sum = np.append(list_sum, int(id))
        rest = subsets[1]
        subset = rest.split(";")

        temp = []

        for sub in subset:
            sub = sub.strip().split(",")
            temp.append(sub)

        cubes = temp

        max_red = 0
        max_green = 0
        max_blue = 0

        for i, cube in enumerate(cubes):
            for j, c in enumerate(cube):
                check = c.strip().split(" ")

                if check[1] == "red":
                    if int(check[0]) > max_red:
                        max_red = int(check[0])
                elif check[1] == "green":
                    if int(check[0]) > max_green:
                        max_green = int(check[0])
                elif check[1] == "blue":
                    if int(check[0]) > max_blue:
                        max_blue = int(check[0])

            max_color = max_red * max_green * max_blue

        list_max = np.append(list_max, max_color)

print(f"Part 2: {int(np.sum(list_max))}")
