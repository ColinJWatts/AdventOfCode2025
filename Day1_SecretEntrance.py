get_input = lambda filename: [l.strip('\n') for l in open(filename,'r',encoding='utf-8').readlines()]

# datafile = "test"
datafile = "Day1Data"

raw = get_input(f"data/{datafile}.txt")

dirs = []
counts = []

for r in raw:
    dirs.append(r[0])
    counts.append(int(r[1:]))

dialLoc = 50
dialLoc2 = 50

dial = [x for x in range(100)]

print(f"Dial starts at {dial[dialLoc]}")

zeroCount = 0
zeroClicks = 0

for i in range(len(dirs)):
    dir = dirs[i]
    count = counts[i]

    if dir == "R":
        dialLoc = (dialLoc + count) % len(dial)
    else:
        dialLoc = dialLoc - count
        while dialLoc < 0:
            dialLoc = len(dial) + dialLoc

    # part 2
    for j in range(count):
        if dir == "R":
            dialLoc2 += 1
            if dialLoc2 >= len(dial):
                dialLoc2 = 0
        else:
            dialLoc2 -= 1
            if dialLoc2 < 0:
                dialLoc2 = len(dial) - 1
        if dialLoc2 == 0:
            zeroClicks += 1
    
    print(f"Turn dial {dir} by {count} clicks to {dial[dialLoc]}")
    
    if (dialLoc == 0):
        zeroCount += 1

print(f"Hit zero {zeroCount} times")
print(f"{zeroClicks} total times past zero")