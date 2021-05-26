input_cnt = int(input())
input_matrix = [list(map(int, input())) for _ in range(input_cnt)]


# visited : 방문내역 저장
visited = [[0]*input_cnt for _ in range(input_cnt)]
# 좌/우/상/하 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = 1       # 방문 여부 표시
    global cnt             # 아파트 단지 수를 셈 (단지에 아파트가 있으면 +1)
    if input_matrix[x][y] == 1:
        cnt += 1
        
    # 해당 위치에서 좌/우/상/하 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (0 <= new_x < input_cnt) & (0 <= new_y < input_cnt) :
            if (visited[new_x][new_y] == 0) & (input_matrix[new_x][new_y] == 1):
                dfs(new_x, new_y)

cnt = 0      # 아파트 수
numlist = [] # 단지별 아파트 수

for xx in range(input_cnt):
    for yy in range(input_cnt):
        if (input_matrix[xx][yy] == 1) & (visited[xx][yy] == 0) :
            dfs(xx, yy)
            print(xx, yy, cnt)
            numlist.append(cnt)
            cnt = 0

print(len(numlist))
for n in sorted(numlist):
    print(n)