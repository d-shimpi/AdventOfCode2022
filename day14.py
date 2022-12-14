day14text = open('day14.txt','r')
rockLines = day14text.readlines()
import numpy as np
length = 800
grid = np.zeros((200,length))
grid = grid.tolist()
sand_placed = 0
max_x = 173
floor = max_x + 2

for rockLine in rockLines:
    rockLine = rockLine[:-1]
    rock_coords = rockLine.split('->')
    prev_rock_coords = rock_coords[0].strip().split(',')
    prev_x = int(prev_rock_coords[1])
    prev_y = int(prev_rock_coords[0])
    for rock_coord in rock_coords:
        rock_coord = rock_coord.strip()
        rock = rock_coord.split(',')
        x = int(rock[1])
        y = int(rock[0])
        grid[x][y] = 1
        # Fill in blanks between previous rock coordinate
        for space in range(min(x,prev_x),max(x,prev_x)):
            grid[space][y] = 1
        for space in range(min(y,prev_y),max(y,prev_y)):
            grid[x][space] = 1
        prev_x = x
        prev_y = y

sand_start_y = 500
sand_start_x = 0

#Drop some sand
last_sand_x = 0
while last_sand_x < max_x:
    curr_sand_x = 0
    curr_sand_y = sand_start_y
    sand_moving = True
    # Move the sand
    while (sand_moving):
        if curr_sand_x > max_x:
            break
        # Check below
        if (grid[curr_sand_x + 1][curr_sand_y] == 0):
            curr_sand_x = curr_sand_x + 1
            continue
        # Check below to left
        if (grid[curr_sand_x + 1][curr_sand_y - 1] == 0):
            curr_sand_x  = curr_sand_x + 1
            curr_sand_y = curr_sand_y - 1
            continue
        # Check below to right
        if (grid[curr_sand_x + 1][curr_sand_y + 1] == 0):
            curr_sand_x  = curr_sand_x + 1
            curr_sand_y = curr_sand_y + 1
            continue
        # If none of the above
        sand_moving = False
    # Place sand
    if curr_sand_x > max_x:
        break
    grid[curr_sand_x][curr_sand_y] = 2
    sand_placed += 1
    last_sand_x = curr_sand_x
print("Sand blocks placed: " + str(sand_placed))
grid[floor] = [1]*length

# PART 2 I"M TOO LAZY TO PUT STUFF INTO FUNCTIONS SO I"M REPEATING CODE

while last_sand_x > 0:
    curr_sand_x = 0
    curr_sand_y = sand_start_y
    sand_moving = True
    # Move the sand
    while (sand_moving):
        # Check below
        if (grid[curr_sand_x + 1][curr_sand_y] == 0):
            curr_sand_x = curr_sand_x + 1
            continue
        # Check below to left
        if (grid[curr_sand_x + 1][curr_sand_y - 1] == 0):
            curr_sand_x  = curr_sand_x + 1
            curr_sand_y = curr_sand_y - 1
            continue
        # Check below to right
        if (grid[curr_sand_x + 1][curr_sand_y + 1] == 0):
            curr_sand_x  = curr_sand_x + 1
            curr_sand_y = curr_sand_y + 1
            continue
        # If none of the above
        sand_moving = False
    # Place sand
    grid[curr_sand_x][curr_sand_y] = 2
    sand_placed += 1
    last_sand_x = curr_sand_x
print("Sand blocks placed: " + str(sand_placed))


