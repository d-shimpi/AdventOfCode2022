import networkx as nx

day12text = open('day12.txt','r')
mountainLines = day12text.readlines()


def checkAlt(current,possible):
    if possible == 'S':
        return True
    elif possible == 'E':
        if current in ['y','z']:
            return True
        else:
            return False
    else:
        if current == 'S':
            if possible in ['a','b']:
                return True
            else:
                return False
        else:
            return ord(current) >= ord(possible) - 1


indexS = ''
indexE = ''
indexAs = []
G = nx.DiGraph()
for i in range(0,len(mountainLines)):
    mountains = mountainLines[i][:-1]
    for j in range(0,len(mountains)):
        di_edges = []
        currPos = mountainLines[i][j]
        currIndex = str(i) + "_" + str(j)
        if currPos == 'S':
            indexS = str(i) + "_" + str(j)
            indexAs.append(indexS)
        if currPos == 'E':
            indexE = str(i) + "_" + str(j)
        if currPos == 'a':
            indexAs.append(currIndex)
        #Check above
        if (i > 0):
            if checkAlt(currPos,mountainLines[i-1][j]):
                tempPos = str(i-1) + "_" + str(j)
                di_edges.append((currIndex,tempPos))
        #Check below
        if (i < len(mountainLines) - 1):
            if checkAlt(currPos,mountainLines[i+1][j]):
                tempPos = str(i+1) + "_" + str(j)
                di_edges.append((currIndex,tempPos))
        #Check left
        if (j > 0):
            if checkAlt(currPos,mountainLines[i][j-1]):
                tempPos = str(i) + "_" + str(j-1)
                di_edges.append((currIndex,tempPos))
        #Check right
        if (j < len(mountains) - 1):
            if checkAlt(currPos,mountainLines[i][j+1]):
                tempPos = str(i) + "_" + str(j+1)
                di_edges.append((currIndex,tempPos))
        G.add_edges_from(di_edges)
steps = nx.shortest_path_length(G,indexS,indexE)
print("The shortest path from S to E takes " + str(steps) + " steps.")

stepsAtoE = []
for indexA in indexAs:
    if (nx.has_path(G, indexA, indexE)):
        stepsAtoE.append(nx.shortest_path_length(G,indexA,indexE))
minAtoE = min(stepsAtoE)
print("The shortest path from any a to E takes " + str(minAtoE) + " steps.")





