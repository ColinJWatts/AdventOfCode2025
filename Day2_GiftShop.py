get_input = lambda filename: [l.strip('\n') for l in open(filename,'r',encoding='utf-8').readlines()]

datafile = "test"
datafile = "Day2Data"

raw = get_input(f"data/{datafile}.txt")

rangeStrings = raw[0].split(",")
ranges = []

for rs in rangeStrings:
    temp = rs.split("-")
    ranges.append((int(temp[0]), int(temp[1])))


def part1():
    ans = 0

    for r in ranges:
        for x in range(r[0], r[1] + 1, 1):
            temp = str(x)
            if len(temp) % 2 == 0:
                part1 = temp[:int(len(temp)/2)]
                part2 = temp[int(len(temp)/2):]

                if part1 == part2:
                    ans += x

    print(ans)

def part2():
    ans = 0

    for r in ranges:
        for x in range(r[0], r[1] + 1, 1):
            temp = str(x)
            isInvalid = False
            for y in range(1, int(len(temp)/2)+1):
                if len(temp) % y == 0 and not isInvalid:
                    # can break string into groups of y
                    groups = [temp[i:i+y] for i in range(0, len(temp), y)]
                    prevGroup = groups[0]
                    allMatch = True
                    for i in range(1, len(groups), 1):
                        if prevGroup != groups[i]:
                            allMatch = False
                        prevGroup = groups[1]
                    if allMatch:
                        print(f"{x} {y}: {groups}")
                        ans += x
                        isInvalid = True
    
    print(ans)

part2()