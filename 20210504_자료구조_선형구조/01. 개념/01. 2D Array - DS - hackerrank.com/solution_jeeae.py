def hourglassSum(arrr):
  import numpy as np

  arr_sum = []
  for i in range(4):
    for j in range(4):
      arr_sum.append(np.multiply(arrr[:3,:3]!=0, arrr[i:(i+3),j:(j+3)]).sum())
  maxsum = max(arr_sum)
  return maxsum