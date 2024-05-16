import numpy as np

list_to_sum = np.array([])
list_to_sum_2 = np.array([])

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
numbers_letter = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

# part 1
with open("input.txt") as file:
    for line in file:
        list_line = []
        for i in range(len(line)):
            if line[i] in numbers:
                list_line.append(line[i])

        number_to_add = list_line[0] + list_line[-1]
        list_to_sum = np.append(list_to_sum, int(number_to_add))

part1 = int(np.sum(list_to_sum))
print(f"Part 1: {part1}")


# part 2
with open("input.txt") as file:
    for line in file:
        list_line = []

        for i in range(len(line)):
            if line[i] in numbers:
                list_line.append(line[i])

            if (i + 3) < len(line):
                if line[i : i + 3] in numbers_letter:
                    list_line.append(numbers_letter[line[i : i + 3]])

            if (i + 4) < len(line):
                if line[i : i + 4] in numbers_letter:
                    list_line.append(numbers_letter[line[i : i + 4]])

            if (i + 5) < len(line):
                if line[i : i + 5] in numbers_letter:
                    list_line.append(numbers_letter[line[i : i + 5]])

        number_to_add = list_line[0] + list_line[-1]
        list_to_sum_2 = np.append(list_to_sum_2, int(number_to_add))

part2 = int(np.sum(list_to_sum_2))
print(f"Part 2: {part2}")
