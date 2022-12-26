import csv

graph = dict()


def addLocation(a, b, distance):
    if a not in graph:
        graph[a] = [(b, distance)]
    else:
        graph[a].append((b, distance))


with open("D:\Assignment\Assignment-1\Code\distance_lib.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        a, b = row[0].split("-")
        addLocation(a, b, int(row[1]))
        addLocation(b, a, int(row[1]))

print(graph)