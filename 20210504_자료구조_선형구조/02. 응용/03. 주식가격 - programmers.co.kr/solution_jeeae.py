# 첫 번째 코드
def solution(prices):
  res = []
  for i, p in enumerate(prices):
    t = 0
    for after_p in prices[(i+1):]:
      if p <= after_p:
        t += 1
      else:
        pass
    res.append(t)
  return res


#------------------------------------------
# 두 번째 코드
def solution(prices):
  from collections import deque

  deq = deque(prices)
  res = []
  while len(deq):
    t = 0
    p = deq.popleft()
    deq_after = deq.copy()
    while len(deq_after):
      if p <= deq_after.popleft():
        t += 1
    res.append(t)
  return res