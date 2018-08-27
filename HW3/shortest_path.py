from heapq import *
from collections import defaultdict

def trans(lines):
    trans = []
    for i in range(len(lines)):
        if i%2 == 1:
            for j in range(len(lines[i])):
                if lines[i][j]=='(':
                    if lines[i][j+3]!='-':
                        trans.append((lines[i-1][0],lines[i][j+1],lines[i][j+3]))
                    else:
                        trans.append((lines[i-1][0],lines[i][j+1],lines[i][j+3]+lines[i][j+4]))
    return trans
    
def find_shortest_path(name_txt_file,source,destination):
    files = open('name_txt_file','r')
    lines = files.readlines()
    tran = trans(lines)
    edges = defaultdict(list)
    weights = {}
    for each in tran:
        edges[each[0]].append(each[1])
        weights[(each[0],each[1])] = each[2]
    
    q = [(0,source,str(source))]
    visited = set()
    dist = {source:0}
    while q:
        for item in q:
            if edges.get(str(item[1]))==None and item[1]!=str(destination):
                q.remove(item)
            else:
                q = q
        if edges.get(str(source))==None:
            print("No next node found.")
        else:
            (cost,v1,path) = heappop(q)
            if v1 not in visited:
                visited.add(v1)
                if int(v1) == destination:
                    return(cost,path.split())
                else:
                    for v2 in edges.get(str(v1)):
                        if v2 not in visited:
                            cost = dist[v1] + int(weights.get((str(v1),str(v2))))
                            dist[v2] = cost
                            path1 = path+','+str(v2)
                            heappush(q,(dist[v2],v2,path1))
                       
                        elif dist[v1] + int(weights.get((str(v1),str(v2)))) < dist[v2]:
                            cost = dist[v1] + int(weights.get((str(v1),str(v2))))
                            dist[v2] = cost
