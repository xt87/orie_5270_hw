def trans(lines):
    trans = []
    for i in range(len(lines)):
        if i%2 == 1:
            if lines[i]=='\n':
                trans.append((lines[i-1][0],lines[i],lines[i]))  
            else:
                for j in range(len(lines[i])):
                    if lines[i][j]=='(':
                        if lines[i][j+3]!='-':
                            trans.append((lines[i-1][0],lines[i][j+1],lines[i][j+3]))
                        else:
                            trans.append((lines[i-1][0],lines[i][j+1],lines[i][j+3]+lines[i][j+4]))
            
            
    return trans
    
def find_negative_cycles(name_txt_file):
    files = open('name_txt_file','r')
    lines = files.readlines()
    tran = trans(lines)
    edges = defaultdict(list)
    weights = {}
    for each in tran:
        edges[each[0]].append(each[1])
        weights[(each[0],each[1])] = each[2]
    
    for node in edges.keys():
        d = {}
        p = {}
        for node in edges.keys():
            d[node] = float('Inf')
            p[node] = None
    
    i=0
    while i<len(edges.keys())-1:
        for node in edges.keys():
            d[node]=0
            if edges.get(node) != ['\n']:
                for neighbour in edges.get(node):
                    if d[neighbour] > d[node] + int(weights.get((node,neighbour))):
                        d[neighbour] = d[node] + int(weights.get((node,neighbour)))
                        p[neighbour] = node
            else:
                pass
        i = i+1
    
    negative_cycle=[]
    for node in d.keys():
        if d[node]<0:
            print('Found a negative cycle.')
            start = node
            negative_cycle=[start]
            backward = p[start]
            while backward != start and backward:
                negative_cycle.append(backward)
                backward = p[backward]
            return negative_cycle
        else:
            return None
