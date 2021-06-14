#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = 0
    answer = num + 1
    tmp = list(str(answer))
    tmp2 = ''
    
    for i, n in enumerate(tmp):
        if int(n)==0:
            tmp[i]=str(1)
        tmp2 += tmp[i]
    
    answer = int(tmp2)
    
    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")