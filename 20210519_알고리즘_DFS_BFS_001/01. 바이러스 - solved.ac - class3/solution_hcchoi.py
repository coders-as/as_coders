def dfs(tree, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
      
    visit.remove(start_node)
    
    return len(visit)

n = int(input('Number of nodes : '))
m = int(input('Number of edges : '))

graph ={(i+1):[] for i in range(n)}

for i in range(m):
    a, b = map(int, input('Connect nodes : ').split())
    
    if a in graph:
        graph[a].append(b)
        
dfs(graph, 1)