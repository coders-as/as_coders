def solution(n):
  a = ['', '1', '2', '4']
  res = ''
  while n:
    res = a[n%3 + (n%3 == 0)*3] + res
    n = n//3 - (n%3 == 0)
  return res