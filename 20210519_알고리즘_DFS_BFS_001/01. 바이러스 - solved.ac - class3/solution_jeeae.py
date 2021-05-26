a = int(input())  # 컴퓨터의 수
b = int(input())  # 직접 연결된 컴퓨터 쌍의 수

tree = {(i+1):[] for i in range(a)}
for _ in range(b):
  m,n = map(int, input().split())
  tree[m].append(n)
  tree[n].append(m)


from collections import deque

def bfs_count1(tree, start_node):
  q = deque()
  q.append(start_node)
  visit = []

  cnt = 0
  while q:
    node = q.popleft()
    if node==1: cnt += len(tree[node])   # key=1일 때 카운트
    if node not in visit:
      visit.append(node)
      for next in tree[node]:
        if next==1: cnt += 1  # value=1일 때 카운트
        if next not in visit:  # queue 목록 중에서 1(visited)인 경우 제외
          q.append(next)
  return cnt