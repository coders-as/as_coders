#You may use import as below.
#import math

def solution(num):
    # Write code here.
    num_1 = num + 1
    str_num = str(num_1);
    str_num = str_num.replace('0','1')
    answer = int(str_num)
 
    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")