#---------------------------#
# 각 숫자별로 연결되는 숫자를 연결
# - computer_cnt : 숫자 개수 (7)
# - pair_cnt : 쌍의 개수     (6)
#---------------------------#
computer_cnt = int(input())
pair_cnt = int(input())
graph_list = []
for i in range(computer_cnt + 1):
    graph_list.append([])
for _ in range(pair_cnt) :
    start, end = map(int, input().strip().split())
    graph_list[start].append(end)
    graph_list[end].append(start)
    
    
from collections import deque

def bfs(graph_list) :
    #-------------------------#
    # 데크(deque) : 양방향 큐
    #-------------------------#
    check_que = deque([1])
    visited = []
    
    while check_que :
        check_num = check_que.popleft()
        if check_num not in visited :
            visited.append(check_num)
            check_que.extend(graph_list[check_num])
        print(check_num, visited, check_que)
    return visited


    
result = bfs(graph_list)
print(len(result)-1)