import re

with(open('input.txt', 'r')) as file:
	lines = file.readlines()

regex = r'(-?\d+)'

numbers = []
for line in lines:
	numbers.append(re.findall(regex, line))


def search_zeros(numbers: list) -> list:

	line = []
	new = []

	line.append(numbers[-1])

	for i in range(len(line[-1]) - 1):
		new.append(int(line[-1][i+1]) - int(line[-1][i]))

	if all(num ==0 for num in line[-1]):
		return numbers
	
	else:
		numbers.append(new)
		return search_zeros(numbers)
	
def search_numbers(numbers: list) -> list:

	if len(numbers) == 1:
		return numbers
	
	line = numbers[-1]
	above = numbers[-2]

	if all(num == 0 for num in line):
		line.append(0)
	
	above.append(above[-1] + line[-1])
	numbers.pop(-1)

	return search_numbers(numbers)

def search_numbers2(numbers: list) -> list:

	if len(numbers) == 1:
		return numbers
	
	line = numbers[-1]
	above = numbers[-2]

	if all(num == 0 for num in line):
		line.insert(0, 0)
	
	above.insert(0, above[0] - line[0])
	numbers.pop(-1)

	return search_numbers2(numbers)

def part1():
	
	score = 0
	for num in numbers:
		for i in range(len(num)):
			num[i] = int(num[i])
			
		encapsulated = []
		encapsulated.append(num)
		result = search_zeros(encapsulated)
		new_result = search_numbers(result)
		score += new_result[0][-1]

	print('part 1:', score)


def part2():
	
	score = 0
	for num in numbers:
		for i in range(len(num)):
			num[i] = int(num[i])
		
		encapsulated = []
		encapsulated.append(num)
		result = search_zeros(encapsulated)
		new_result = search_numbers2(result)
		score += new_result[0][0]

	print('part 2:', score)


part1()
part2()

