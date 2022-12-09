day9txt = open('day9.txt','r')
movements = day9txt.readlines()

#Define some useful helper functions
def checkTailHead(head,tail):
    x_diff = abs(head[0] - tail[0])
    y_diff = abs(head[1] - tail[1])
    
    if (x_diff > 1 or y_diff > 1):
        return True
    else:
        return False
    
def moveHead(head,direc):
    if (direc == 'U'):
        head = [head[0], head[1] + 1]
    elif (direc == 'D'):
        head = [head[0], head[1] - 1]
    elif (direc == 'L'):
        head = [head[0] - 1, head[1]]
    else:
        head = [head[0] + 1, head[1]]
    return head
    
def hashList(tail):
    return str(tail[0]) + "_" + str(tail[1])

def moveBody(head,tail):
    # This function is only hit if we know we have to move, i.e.
    # abs(x_diff) > 1 or abs(y_diff) > 1
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    x_sign = 0
    y_sign = 0
    
    if x_diff < 0:
        x_sign = -1
    else:
        x_sign = 1
    if y_diff < 0:
        y_sign = -1
    else:
        y_sign = 1
    
    
    #Handle vertical
    if (x_diff == 0):
        tail[1] = tail[1] + y_sign
        return tail
    #Handle horizontal
    elif (y_diff == 0):
        tail[0] = tail[0] + x_sign
        return tail
    #Handle diagonal
    else:
        tail[1] = tail[1] + y_sign
        tail[0] = tail[0] + x_sign
        return tail


x = 0 #starting position
y = 0 #starting position
head = [x,y]
tail = [x,y]
prev_head = [x,y]
tail_places = {hashList(tail)}
for movement in movements:
    #Read in movement
    direction = movement.split()[0]
    magnitude = int(movement.split()[1])
    
    for i in range(0,magnitude):
        #Move head
        head = moveHead(head,direction)
        #Check head tail
        moveTail = checkTailHead(head,tail)
        #Update tail if necessary
        if moveTail:
            #tail = prev_head
            tail = moveBody(head,tail)
            tail_places.add(hashList(tail))
        prev_head = head

print("Number of unique tail locations: " + str(len(tail_places)))

# ------------------------
# PART 2
# ------------------------    

#Example for debugging :(
ex = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

example_moves = ex.split('\n')

x = 0 #starting position
y = 0 #starting position
rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
prev_rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

final_tail_places = {hashList([0,0])}
for movement in movements:
#for movement in movements:
    #Read in movement
    direction = movement.split()[0]
    magnitude = int(movement.split()[1])
    
    for i in range(0,magnitude):
        #Move head
        rope[0] = moveHead(rope[0],direction)
        #print(rope[0])
        #Check all other parts of the rope
        for i in range(1,len(rope)):
            moveSection  = checkTailHead(rope[i-1],rope[i])
            if moveSection:
                # NEED TO HANDLE MOVEMENT DIFFERENT
                rope[i] = moveBody(rope[i-1],rope[i])
                if (i == 9):
                    final_tail_places.add(hashList(rope[i]))
            prev_rope[i-1] = rope[i-1]

print("Total unique places the last segment visited: " + str(len(final_tail_places)))