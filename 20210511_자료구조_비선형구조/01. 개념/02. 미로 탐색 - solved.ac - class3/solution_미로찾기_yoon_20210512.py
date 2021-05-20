#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sys   
N,M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)] 


# In[36]:


from collections import deque  
def bfs(N, M, graph):
    visited = [] # 방문 기록
    q = deque() # FIFO 
    q.appendleft([[0,0],1]) # [[x,y좌표], cnt(이동횟수)]
    
    dx = (-1,0,1,0)# x탐색
    dy = (0,1,0,-1)# y탐색
    while(q): # q가 없어질때까지 돌아
        node = q.pop() #현재 node, 오른쪽에 있는거 제거
        # 방문한 기록이 있는지 확인
        if node[0] not in visited:
            visited.append(node[0]) # 방문 기록
            for i in range(4): 
                # 현재 노드 기준으로 동서남북 네 방향에 대해 bfs
                new_x = node[0][0] + dx[i]
                new_y = node[0][1] + dy[i] 
                
                if 0<=new_x<N and 0<=new_y<M and graph[new_x][new_y]==1: 
                    if new_x==N-1 and new_y==M-1:
                        return node[1] + 1 #node 업뎃 
                    else:
                        q.appendleft([[new_x, new_y], node[1]+1])
                        # 출구에 도착한 것이 아니라면 queue에 추가한다.
    return node[1]#
 


# In[37]:


bfs(N, M,maze)

