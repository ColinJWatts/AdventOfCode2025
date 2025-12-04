get_input = lambda filename: [l.strip('\n') for l in open(filename,'r',encoding='utf-8').readlines()]

datafile = "test"
datafile = "Day3Data"

raw = get_input(f"data/{datafile}.txt")

powerBanks = []

for r in raw:
    powerBank = []
    for d in r:
        powerBank.append(int(d))
    powerBanks.append(powerBank)

def part1():
    ans = 0

    for powerBank in powerBanks:
        maxFront = powerBank[-2]
        maxTrailing = powerBank[-1]
        for i in range(len(powerBank)-3, -1, -1):
            if powerBank[i] >= maxFront:
                if maxFront > maxTrailing:
                    maxTrailing = maxFront
                maxFront = powerBank[i]
        ans += int(str(maxFront) + str(maxTrailing))

    print(f"Total Joltage: {ans}")

def part2():
    ans = 0

    for powerBank in powerBanks:
        maxes = powerBank[-12:]
        for i in range(len(powerBank)-13, -1, -1):
            curr = powerBank[i]
            for j in range(len(maxes)):
                if curr >= maxes[j]:
                    temp = curr
                    curr = maxes[j]
                    maxes[j] = temp
                else:
                    break
        
        joltString = ""
        for s in maxes:
            joltString += str(s)
        ans += int(joltString)
        print(joltString)

    print(f"Total Joltage: {ans}")

part2()