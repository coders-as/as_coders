# dfs에서 stack에 쌓을 때 역순으로..(reversed)  ????????
def dfs(tree, start_node):

  visit = []
  stack = []
  stack.append(start_node)

  while stack:
    node = stack.pop()
    if node not in visit:
      visit.append(node)
      stack.extend(reversed(tree[node]))   # 역순
  return visit

def bfs(tree, start_node):
  from queue import Queue
  visit = []
  q = Queue()
  q.put(start_node)

  while q.qsize() > 0:
    node = q.get()
    if node not in visit:
      visit.append(node)
      for nextNode in tree[node]:
        q.put(nextNode)
  return visit

n,m,v = map(int, input().split()) 
# a,b = map(int, input().split())

# 트리만들기
graph ={(i+1):[] for i in range(n)}
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for x in graph:
  graph[x].sort()

print(' '.join(map(str, dfs(graph, v))))
print(' '.join(map(str, bfs(graph, v))))