h, m = map(int, input().split())
if m < 45:
  h_new = 23 if h==0 else h-1
  m_new = m + 60 - 45
else:
  h_new = h
  m_new = m - 45
print(h_new, m_new)