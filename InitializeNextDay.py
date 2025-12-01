import os
import requests
import webbrowser

files = [x for x in os.listdir("./") if os.path.isfile(x) and x[:3] == "Day"]
sessionId = open("./data/sessionId.txt", 'r').read()

daynums = []
maxNum = 0
for fileName in files:
    [day, title] = fileName.split("_", 1)
    daynums.append(int(day[3:]))
    if daynums[-1] > maxNum:
        maxNum = daynums[-1]
daynum = maxNum + 1

print(f"Getting data for day {daynum}")

webbrowser.open(f"https://adventofcode.com/2025/day/{daynum}")

print("Input Title Now")
title = input().strip().replace(" ", "_")

with open(f"Day{daynum}_{title}.py", 'w') as f:
    f.writelines(["get_input = lambda filename: [l.strip('\\n') for l in open(filename,'r',encoding='utf-8').readlines()]\n\n", 
                 'datafile = "test"\n',
                 f'# datafile = "Day{daynum}Data"\n\n',
                 'raw = get_input(f"data/{datafile}.txt")\n\n'])

dataResponse = requests.get(f"https://adventofcode.com/2025/day/{daynum}/input", cookies={'session': sessionId})

with open(f"./data/Day{daynum}Data.txt",'w') as datafile:
    datafile.write(dataResponse.text)
