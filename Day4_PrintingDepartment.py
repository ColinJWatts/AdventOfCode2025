get_input = lambda filename: [l.strip('\n') for l in open(filename,'r',encoding='utf-8').readlines()]

datafile = "test"
datafile = "Day4Data"

raw = get_input(f"data/{datafile}.txt")

grid = []
ymax = len(raw)
xmax = len(raw[0])

for row in raw:
    grid.append([])
    for col in row:
        grid[-1].append(col)


def printGrid(toPrint):
    for y in range(ymax):
        line = ""
        for x in range(xmax):
            line += toPrint[y][x]
        print(line)

def getValueAtLocation(x, y, toCheck):
    if x < 0 or x >= xmax:
        return None
    if y < 0 or y >= ymax:
        return None
    return toCheck[y][x]

locationsToCheck = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

def part1():  
    numReachable = 0

    testGrid = []

    for y in range(ymax):
        testGrid.append([])
        for x in range(xmax):
            testGrid[-1].append(grid[y][x])
            if grid[y][x] == '@':
                numAdjacent = 0
                for toCheck in locationsToCheck:
                    tc = getValueAtLocation(x + toCheck[0], y + toCheck[1], grid)
                    if not tc is None and tc == '@':
                        numAdjacent += 1
                if numAdjacent < 4:
                    numReachable += 1
                    testGrid[-1][-1] = 'x'

    printGrid(testGrid)
    print(f"Forklift Can Reach {numReachable} rolls")

def part2():
    numReachable = 0

    anyRemoved = True
    currGrid = grid

    while anyRemoved:
        anyRemoved = False
        nextGrid = []

        for y in range(ymax):
            nextGrid.append([])
            for x in range(xmax):
                nextGrid[-1].append(currGrid[y][x])
                if currGrid[y][x] == '@':
                    numAdjacent = 0
                    for toCheck in locationsToCheck:
                        tc = getValueAtLocation(x + toCheck[0], y + toCheck[1], currGrid)
                        if not tc is None and tc == '@':
                            numAdjacent += 1
                    if numAdjacent < 4:
                        numReachable += 1
                        nextGrid[-1][-1] = '.'
                        anyRemoved = True
        currGrid = nextGrid
        # printGrid(nextGrid)
        # print()
    print(f"Forklift Can Reach {numReachable} rolls")

part2()