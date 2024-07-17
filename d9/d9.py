import re

with(open('input.txt', 'r')) as file:
	lines = file.readlines()

regex = r'-?(\d+)'

numbers = []
for line in lines:
	numbers.append(re.findall(regex, line))


