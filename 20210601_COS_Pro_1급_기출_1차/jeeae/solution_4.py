#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = str(num + 1)
    answer = int(answer.replace('0','1'))
    return answer

#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")