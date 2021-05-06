from datetime import datetime


def read_plan(file):

    with open(file, "r") as f:
        planning = f.readline()
        while planning:
            planning = f.readline()
            newline = planning.strip().split()
            if planning != []:
                print(newline)

# read_plan("planning.log")


def pourcent(start, end):
    read_plan("planning.log")
    with open("expected_output.txt", "r") as f:
        # s1 = newline[0]
        # s2 = newline[1]
        FM = '%H:%M'
        tdelta = datetime.strptime(end, FM) - datetime.strptime(start, FM)
pourcent('11:30', '12:30')
