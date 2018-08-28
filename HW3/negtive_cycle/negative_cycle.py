def trans(lines):
    trans = []
    for i in range(len(lines)):
        if i%2 == 1:
            if lines[i]=='\n':
                trans.append((float(lines[i-1][0]),None,None)) 
            else:
                for j in range(len(lines[i])):
                    if lines[i][j]=='(':
                        if lines[i][j+3]!='-':
                            trans.append((float(lines[i-1][0]),float(lines[i][j+1]),float(lines[i][j+3])))
                        else:
                            trans.append((float(lines[i-1][0]),float(lines[i][j+1]),float(lines[i][j+3]+lines[i][j+4])))
            
            
    return trans
    
def find_negative_cycles(name_txt_file):
    files = open(name_txt_file,'r')
    lines = files.readlines()
    tran = trans(lines)
    edges = defaultdict(list)
    weights = {}
    for each in tran:
        edges[each[0]].append(each[1])
        weights[(each[0],each[1])] = each[2]
    
    for source in edges.keys():
        d = {}
        p = {}
        for other_node in edges.keys():
            d[other_node] = float('Inf')
            p[other_node] = None
        d[source]=0
    
        for i in range(len(edges.keys())-1):
            for node in edges.keys():
                if edges.get(node) != [None]:
                    for neighbour in edges.get(node):
                    #print(neighbour,'b')
                        if d[neighbour] > d[node] + int(weights.get((node,neighbour))):
                            d[neighbour] = d[node] + int(weights.get((node,neighbour)))
                            p[neighbour] = node
  
        for node in edges.keys():
            if edges.get(node) != [None]:
                for neighbour in edges.get(node):
                    if d[neighbour] > d[node] + int(weights.get((node,neighbour))):
                        #print('Found a negative cycle')
                        negative_cycle=[node]
                        back = p[node]
                        while node != back and back:
                            negative_cycle.append(back)
                            back = p[back]
                        negative_cycle.append(back)
                        negative_cycle[::-1]
                        return negative_cycle
    return None
