import re
import math

with(open('input.txt', 'r') as file):
    lines = file.readlines()

path = lines[0].strip()

nodes = { }
for line in lines[1:]:  
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    conn = re.findall(regex, line)
    for node, left, right in conn:
        nodes[node] = (left, right)

current = 'AAA'
end = 'ZZZ'

counter = 0

while current != end:
    for char in path:
        counter += 1
        
        if counter > 1_000_000:
            break

        if char == 'L':
            current = nodes[current][0]
            if current == end:
                break

        if char == 'R':
            current = nodes[current][1]
            if current == end:
                break

print('part1', counter)

starting_nodes = []

for node in nodes:
    if node[2] == "A":
        starting_nodes.append(node)

#print(starting_nodes)

def isFinished(starting_nodes):

    for node in starting_nodes:
        if node[2] != "Z":
            return False
        if node[2] == "Z":
            continue
    return True
        
counter = 0


# test = ['CMZ', 'BHZ', 'AAZ', 'DIZ']
# test2 = ['CMZ', 'BHA', 'AAZ', 'DIZ']

# print(isFinished(test))
# print(isFinished(test2))

# BRUTE FORCE NOT WORKING
# while not isFinished(starting_nodes):
    
#     for char in path:
#         counter += 1

#         if counter > 1_000_000:
#             break

#         for i, node in enumerate(starting_nodes):
#             if char == 'L':
#                 starting_nodes[i] = nodes[node][0]
#                 continue

#             if char == 'R':
#                 starting_nodes[i] = nodes[node][1]
#                 continue
        
#         if isFinished(starting_nodes):
#             print('start', starting_nodes)
#             break


# every starting node has its cycle. Let's find the cycle of each starting node and then find the LCM of all cycles
cycles = []

for node in starting_nodes:
    current = node
    cycle = 0
    counter = 0


    while current[2] != 'Z':
        for char in path:
            counter += 1
            
            if counter > 1_000_000:
                break

            if char == 'L':
                current = nodes[current][0]
                if current[2] == 'Z':
                    break

            if char == 'R':
                current = nodes[current][1]
                if current[2] == 'Z':
                    break
    
    cycles.append(int(counter))
    

# find the LCM of all cycles
n = len(cycles)
ans = int(cycles[0])
for i in range(1, n):
    ans = math.lcm(ans, int(cycles[i]))

print('part2', ans )