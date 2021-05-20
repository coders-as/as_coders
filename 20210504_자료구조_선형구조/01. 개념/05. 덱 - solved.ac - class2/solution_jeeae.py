from collections import deque

deq = deque()
input_num = int(input())
while input_num:
  a = input()
  # print(input_num)
  if a.split(' ')[0] == 'push_front':
    deq.appendleft(int(a.split(' ')[1]))
  elif a.split(' ')[0] == 'push_back':
    deq.append(int(a.split(' ')[1]))
  elif a == 'pop_front':
    print(deq.popleft()) if len(deq) > 0 else print('-1')
  elif a == 'pop_back':
    print(deq.pop()) if len(deq) > 0 else print('-1')bab
  elif a == 'size':
    print(len(deq))
  elif a == 'empty':
    print(str(int(len(deq)==0))) 
  elif a == 'front':
    print(deq[0]) if len(deq) > 0 else print('-1')
  elif a == 'back':
    print(deq[-1]) if len(deq) > 0 else print('-1')
  input_num -= 1