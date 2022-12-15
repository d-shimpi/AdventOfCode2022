# Determine if a point is in bounds
def inBounds(coord):
    return (coord >= min_coord and coord <= max_coord)

# Find adjacent points to the border of a sensor's boundary
def findAdjacentPoints(sensor):
    init_x = sensor[0]
    init_y = sensor[1]
    init_dist = sensor[2]
    new_rad = init_dist + 1
    poss_spaces = []

    for i in range(0,new_rad + 1):
        right_x = init_x + new_rad - i
        upper_y = init_y + i
        left_x = init_x - new_rad + i
        lower_y = init_y - i
        if (inBounds(right_x) and inBounds(upper_y)):
            poss_spaces.append([right_x, upper_y])
        if (inBounds(right_x) and inBounds(lower_y)):
            poss_spaces.append([right_x, lower_y])
        if (inBounds(left_x) and inBounds(upper_y)):
            poss_spaces.append([left_x, upper_y])
        if (inBounds(left_x) and inBounds(lower_y)):
            poss_spaces.append([left_x, lower_y])
    return poss_spaces

# Read in text
day15text = open('day15.txt','r')
sensorLines = day15text.readlines()

# Y row we are concerned with
#y_row = 10
y_row = 2000000
# Places in said row we know x can't be
x_cannot = set([])
# Set for beacon x coordinates which lie in row y
beacon_xs_in_row = set([])

# Bounds for coordinates for part 2
min_coord = 0
#max_coord = 20
max_coord = 4000000
# Dictionary of sensors
sensors = []

for line in sensorLines:
    # Get sensor and beacon coordinates
    sensor = line.split(':')[0]
    closestBeacon = line.split(':')[1]
    sensorCoords = sensor.split()
    sensorX = int(sensorCoords[2][2:-1])
    sensorY = int(sensorCoords[3][2:])
    beaconCoords = closestBeacon.split()
    beaconX = int(beaconCoords[4][2:-1])
    beaconY = int(beaconCoords[5][2:])

    if (beaconY == y_row):
        beacon_xs_in_row.add(beaconX)

    #Determine where a beacon can't be in the desginated line (part 1)
    manhat_dist = abs(beaconX - sensorX) + abs(beaconY - sensorY)
    y_dist = abs(sensorY - y_row)
    diff_dist = manhat_dist - y_dist
    if (manhat_dist >= y_dist):
        x_cannot.add(sensorX)
        for i in range(0,diff_dist):
            x_cannot.add(sensorX - (i + 1))
            x_cannot.add(sensorX + (i + 1))
    sensors.append([sensorX,sensorY,manhat_dist])

# Part 1
# Get rid of any beacons that were already in the row
x_cannot = x_cannot.difference(beacon_xs_in_row)

print("Positions that can't contain a beacon in designated row: " + str(len(x_cannot)))

# Part 2 - We know the beacon has to be like right next to the coverage zone of at least one sensor (worst case is that 
# the dead zone is in the corner of the parallel line of the sensor coverage) So gather boundary + 1 for the
# first sensor and then check each point to see whether it's covered by another sensor. If it is continue, if not it must be it
# based on how the areas interact with one another. Determining which sensor it's adjacent to, however, is not super simple BUT we only
# have like 20 sensors so let's just go through them all



target_x = 0
target_y = 0
for sensor in sensors:
    poss_points = findAdjacentPoints(sensor)
    for point in poss_points:
        flag = 1
        for sensor2 in sensors:
            sensor2x = sensor2[0]
            sensor2y = sensor2[1]
            sensor2dist = sensor2[2]
            dist = abs(sensor2x - point[0]) + abs(sensor2y - point[1])
            if dist <= sensor2dist:
                flag = 0
                break
        if (flag == 1):
            target_x = point[0]
            target_y = point[1]
    if (target_x != 0 or target_y != 0):
        break

tuning_freq = target_x * 4000000 + target_y
print ("The tuning frequency of the distress beacon is: " + str(tuning_freq))



        




    
    

    