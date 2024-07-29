import sys
from PIL import Image, ImageDraw, ImageFont



with(open('input.txt', 'r')) as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

sys.setrecursionlimit(10000)

list_nodes = [[0 for i in range(len(lines))] for j in range(len(lines[0]))]
size = len(list_nodes[0]), len(list_nodes)
pipe = {'|', '-', 'L', 'J', '7', 'F', 'S'}

nodes = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):

        if char == '|':
            if i - 1 < 0 and i + 1 >= size[0]:
                continue

            if i - 1 < 0:
                nodes[(i, j)] = [(i+1, j)]
                continue
            
            if i + 1 >= size[0]:
                nodes[(i, j)] = [(i-1, j)]
                continue

            nodes[(i, j)] = [(i-1, j), (i+1, j)]
        
        if char == '-':
            if j - 1 < 0 and j + 1 >= size[1]:
                continue

            if j - 1 < 0:
                nodes[(i, j)] = [(i, j+1)]
                continue
            
            if j + 1 >= size[1]:
                nodes[(i, j)] = [(i, j-1)]
                continue
            
            nodes[(i, j)] = [(i, j-1), (i, j+1)]
        
        if char == 'L':
            if i - 1 < 0 and j + 1 < 0:
                continue

            if i - 1 < 0:
                nodes[(i, j)] = [(i, j+1)]
                continue
            
            if j + 1 >= size[1]:
                nodes[(i, j)] = [(i-1, j)]
                continue

            nodes[(i, j)] = [(i-1, j), (i, j+1)]
        
        if char == 'J':
            if i - 1 < 0 and j - 1 < 0:
                continue

            if i - 1 < 0:
                nodes[(i, j)] = [(i, j-1)]
                continue 

            if j - 1 < 0:
                nodes[(i, j)] = [(i-1, j)]
                continue

            nodes[(i, j)] = [(i-1, j), (i, j-1)]
        
        if char == '7':
            if i + 1 >= size[0] and j - 1 < 0:
                continue

            if i + 1 >= size[0]:
                nodes[(i, j)] = [(i, j-1)]
                continue
            
            if j - 1 < 0:
                nodes[(i, j)] = [(i+1, j)]
                continue

            nodes[(i, j)] = [(i, j-1), (i+1, j)]
        
        if char == 'F':
            if i + 1 >= size[0] and j + 1 >= size[1]:
                continue

            if i + 1 >= size[0]:
                nodes[(i, j)] = [(i, j+1)]
                continue
            
            if j + 1 >= size[1]:
                nodes[(i, j)] = [(i+1, j)]
                continue
            nodes[(i, j)] = [(i, j+1), (i+1, j)]

        if char == 'S':
            nodes[(i, j)] = (i, j)
            print('start:', (i, j))
            start = (i, j) 
    
connected_to_start = []
# check what are the pipes connected to the start
for node in nodes:
    if start in nodes[node]:
        connected_to_start.append(node)

# add the connected pipes to the start node
nodes[start] = connected_to_start

# eliminate neighbors that are not pipes
for node in nodes:
    list_neighbors = nodes[node]
    # Create a list to store neighbors to be removed
    neighbors_to_remove = []

    for i, neighbor in enumerate(list_neighbors):
        if lines[neighbor[0]][neighbor[1]] == '.':
            neighbors_to_remove.append(neighbor)
    
    # Remove neighbors after iterating
    for neighbor in neighbors_to_remove:
        list_neighbors.remove(neighbor)

# dijkstra algoritm
def dijkstra(graph, source):

    queue = []

    for node in graph:
        graph[node] = {'connected': graph[node], 'distance': float('inf'), 'prev': None}
        queue.append(node)
    
    graph[source]['distance'] = 0 # distance from source to source is 0
    graph[source]['prev'] = 'Start'

    while len(queue) != 0:
        node = min(queue, key=lambda x: graph[x]['distance'])
        queue.remove(node)
        
        for neighbor in graph[node]['connected']:
            
            distance = graph[node]['distance'] + 1
            if distance < graph[neighbor]['distance']:
                graph[neighbor]['distance'] = distance
                graph[neighbor]['prev'] = node

        graph[node]['visited'] = True

    return graph

def fill(list_of_nodes, x, y, color, cur):
   
    if x < 0 or x >= len(list_of_nodes) or y < 0 or y >= len(list_of_nodes[0]):
        return
   
    if cur != list_of_nodes[x][y]: 
        return
   
    list_of_nodes[x][y] = color

    fill(list_of_nodes, x-1, y, color, cur)
    fill(list_of_nodes, x+1, y, color, cur)
    fill(list_of_nodes, x, y-1, color, cur)
    fill(list_of_nodes, x, y+1, color, cur)

def floodFill(list_of_nodes, x, y, color):
    if list_of_nodes[x][y] == color: 
        return list_of_nodes
    
    fill(list_of_nodes, x, y, color, list_of_nodes[x][y])
    return list_of_nodes

def shitty_part2(graph):
    for node in graph:
        list_nodes[node[0]][node[1]] = 1
    
    list_char = [[0 for i in range(len(lines))] for j in range(len(lines[0]))]
    
    for i in range(len(list_nodes)):
        for j in range(len(list_nodes[0])):
            if lines[i][j] == '.':
                list_char[i][j] = ' '
            if lines[i][j] == '|':
                list_char[i][j] = '║'
            if lines[i][j] == '-':
                list_char[i][j] = '═'
            if lines[i][j] == 'L':
                list_char[i][j] = '╚'
            if lines[i][j] == 'J':
                list_char[i][j] = '╝'
            if lines[i][j] == '7':
                list_char[i][j] = '╗'
            if lines[i][j] == 'F':
                list_char[i][j] = '╔'
            if lines[i][j] == 'S':
                list_char[i][j] = 'S'

    for i in range(len(list_nodes)):
        for j in range(len(list_nodes[0])):
            if list_nodes[i][j] != 1:
                list_char[i][j] = ' '

    font_path = '/System/Library/Fonts/Menlo.ttc'
    font = ImageFont.truetype(font_path, 24)

    
    rows, cols = len(lines), len(lines[0])
     # Calculate the size of each character
    max_width = max(font.getbbox(char)[2] for row in lines for char in row)
    max_height = max(font.getbbox(char)[3] for row in lines for char in row)

    # Create a new image with a white background
    img_width = max_width * cols
    img_height = max_height * rows

    # make an image to visualize the area
    img = Image.new('RGB', (img_width, img_height), 'white')

    
    # Create a new image with a white background
    
    draw = ImageDraw.Draw(img)

    # Draw each character at the appropriate position
    for i, row in enumerate(list_char):
        for j, char in enumerate(row):
            draw.text((j * max_width, i * max_height), char, font=font, fill='black')

    img.save('area.png')
    
    list_of_nodes = floodFill(list_nodes, start[0], start[1], 2)


    # make an image to visualize the area
    img = Image.new('RGB', (len(list_of_nodes), len(list_of_nodes[0])), 'white')
    pxls = img.load()
    draw = ImageDraw.Draw(img)
    for i, row in enumerate(list_of_nodes):
        for j, char in enumerate(row):
            if char == 2:
                pxls[j, i] = (0, 0, 0)
            if char == 3:
                pxls[j, i] = (255, 0, 0)

    img.save('new.png')


def main(): 

    # part 1

    graph = dijkstra(nodes, start) 

    list_node_to_pop = []
    # remove the nodes that have infinite distance
    for node in graph:
        if graph[node]['distance'] == float('inf'):
            list_node_to_pop.append(node)
    
    for node in list_node_to_pop:
        graph.pop(node)
            
    # maximum distance
    node = max(graph, key=lambda x: graph[x]['distance'])
    print('part1:', graph[node])
    
    # part 2
    # search for the area inside the loop
    # Flood fill algorithm
    # make a 2D array, fill it with 0, put 1 as the path that delimit the area inside
    
    shitty_part2(graph)

    # flood fill algorithm is not working properly
    # since the pipes can be parallel to each other and thus closing a small area
    # then the flood fill algorithm will not be able to fill the area inside the bigger loop but only the small one
    # Then I searched for a solution, and chosed the one from @mgtezak on github
    # I decided to move on to the next problem and come back to this one later
    # my solution is not even good, since it takes DECADES to run (the part 1 lol)

if __name__ == "__main__":
    
    main()
