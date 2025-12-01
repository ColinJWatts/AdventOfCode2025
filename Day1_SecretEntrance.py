get_input = lambda filename: [l.strip('\n') for l in open(filename,'r+',encoding='utf-8').readlines()]

datafile = "test"
datafile = "# Day1Data"

raw = get_input(f"data/{datafile}.txt")

