#!/usr/bin/env python
# coding: utf-8

# In[41]:


#You may use import as below.
#import math

def solution(num):
    # Write code here.
    num=num+1   
    print(str(num))
    for i in range(len(str(num))):        
        if str(num)[i]=='0' :
#             print(i) 
#             print(10**(len(str(num))-i-1))
            num=num+1*10**(len(str(num))-i-1)# 0인 자리에 1 채워줌
             
    answer = int(num)
    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")

