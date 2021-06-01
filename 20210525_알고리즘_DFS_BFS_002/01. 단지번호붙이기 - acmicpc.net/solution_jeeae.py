n = int(input())
a = [list(map(int, input())) for _ in range(n)]

x = [-1,1,0,0]   # 좌우상하
y = [0,0,1,-1]
visited = [[0]*n for _ in range(n)]

def dfs(m,p):
  visited[m][p] = 1
  if a[m][p]==1: # 단지에 아파트가 있으면 +1
    global cnt
    cnt += 1
  for i in range(4):
    m_new = m + x[i]
    n_new = p + y[i]
    if 0 <= m_new < n and 0 <= n_new < n:
      if visited[m_new][n_new]==0 and a[m_new][n_new]==1:  # 좌우상하에 아파트가 있으면 거기로 옮겨서 재탐색
        dfs(m_new,n_new)

cnt = 0  # 아파트 수
res = [] # 단지별 아파트 수 저장 리스트

for mm in range(n):
  for nn in range(n):
    if visited[mm][nn]==0 and a[mm][nn]==1:
      dfs(mm,nn)
      res.append(cnt)
      cnt = 0  # 좌우상하에 아파트가 더이상 없으면 한 단지 끝

print(len(res))
for x in res:
  print(x) 