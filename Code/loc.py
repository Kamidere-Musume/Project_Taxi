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


def findRoute(graph, a, b):
    work = [{'at':a,'route':[],'distance':0}]
    i = 0
    while i < len(work):
        at = work[i]['at']
        distance = work[i]['distance']
        route = work[i]['route']
        for place in graph[at]:
            if place[0] == b:
                return distance + place[1]
            if not any([i['at'] == place[0] for i in work]):
                work.append({'at':place[0],'route':[*route,place],'distance':distance+place[1]})
        i += 1

