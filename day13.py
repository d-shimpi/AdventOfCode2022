day13text = open('day13ex.txt','r')
packetLines = day13text.readlines()
import re
from functools import cmp_to_key

sumOfCorrectPacketIndices = 0
listOfPackets = [[[2]],[[6]]]

# A function to convert our array of objects into an actual list in python using some nifty little recursion
def convertToList(objArray, origList, index):
    while index < len(objArray):
        obj = objArray[index]
        if obj == '[':
            tempList = []
            newIndex = convertToList(objArray,tempList, index + 1)
            origList.append(tempList)
            index = newIndex + 1
            continue
        elif obj.isnumeric():
            origList.append(int(obj))
            index += 1
            continue
        elif obj == ']':
            return index
        else:
            index += 1 
            continue
    return []

# Take in two packet/lists and determine if the packets are in the correct order based on the rules provided
# Read packets from left to right
# If both are integers, left < right => correct, left > right => incorrect, left == right => go next
# If both are lists, compare item by item following protocol above; If left list runs out of items first, correct
# If right runs out of items first, incorrect, if same length and no comparison yields decision, go next
# If one list and other integer, convert integer to list of length 1 and compare based off two lists
def correctPacketOrder(leftPacket,rightPacket):
    flag = 0 #If flag is 1, return true, -1 false, 0 inconclusive

    for leftObj,rightObj in zip(leftPacket,rightPacket):
        #Check if integers
        if isinstance(leftObj,int) and isinstance(rightObj,int):
            if leftObj == rightObj:
                continue
            elif leftObj > rightObj:
                return -1
            else:
                return 1
        elif isinstance(leftObj,list) and isinstance(rightObj,list):
            flag = correctPacketOrder(leftObj,rightObj)
            if flag != 0:
                return flag
        elif isinstance(leftObj,int):
            flag = correctPacketOrder([leftObj],rightObj)
            if flag != 0:
                return flag
        else:
            flag = correctPacketOrder(leftObj,[rightObj])
            if flag != 0:
                return flag

    if isinstance(leftPacket,list) and isinstance(rightPacket,list):
        if len(leftPacket) < len(rightPacket):
            return 1
        elif len(leftPacket) > len(rightPacket):
            return -1
        else:
            return 0
    else:
        return 0


for i in range(1,len(packetLines)//3 + 1):
    leftPacket = packetLines[(i-1)*3]
    leftPacketObjs = re.split('(,|\[|\])',leftPacket[1:-1])
    leftPacketList = []
    convertToList(leftPacketObjs, leftPacketList,0)

    rightPacket = packetLines[(i-1)*3 + 1]
    rightPacketObjs = re.split('(,|\[|\])',rightPacket[1:-1])
    rightPacketList = []
    convertToList(rightPacketObjs, rightPacketList,0)

    listOfPackets.append(leftPacketList)
    listOfPackets.append(rightPacketList)

    #Do comparison between lists afterwards
    if correctPacketOrder(leftPacketList,rightPacketList) == 1:
        sumOfCorrectPacketIndices += i
print("Sum of correct packet indices: " + str(sumOfCorrectPacketIndices))

sortedPackets = sorted(listOfPackets, key=cmp_to_key(correctPacketOrder))
sortedPackets.reverse()
firstDivIndex = sortedPackets.index([[2]]) + 1
secondDivIndex = sortedPackets.index([[6]]) + 1
print("Decoder Key: " + str(firstDivIndex*secondDivIndex))