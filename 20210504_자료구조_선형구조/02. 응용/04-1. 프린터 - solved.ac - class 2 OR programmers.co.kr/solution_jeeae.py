def solution(p, location):
  from collections import deque

  # p = [2,1,3,4]
  res_dict = dict(((i,x) for i,x in enumerate(p)))
  # res_dict = dict({'A':2,'B':1,'C':3,'D':4})
  res = []
  res_key = []
  deq = deque(p)
  deq_key = deque(res_dict)

  while len(deq):  # 남은 문서가 없을 때까지
    j = deq.popleft()
    j_key = deq_key.popleft()

    if sum([x > j for x in deq if x > j]):  # 남은 문서 중에서 중요도가 높은 문서가 하나라도 있으면
      deq.append(j)
      deq_key.append(j_key)
    else:
      res.append(j)  # 인쇄
      res_key.append(j_key)

  return res_key.index(location)+1



#------------------------------------------
# 다른 사람 풀이
#    : deque 안에 튜플 형태가 가능하므로 dict 안써도 됨....
#    : 남은 문서 중에 찾을 때 loop 말고 max 사용
#    : 인쇄할 때마다 +1 해주고 break 써서 시간 단축
def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer