#You may use import as below.
#import math

def solution(n):
    # Write code here.
    center_list = [1]
    i, m = 1, 1
    while m < n*n :
        add_num = 2*(n-i)
        m += add_num
        center_list.append(m)
        m += add_num
        center_list.append(m)
        i = i+2
    center_list = [num for num in center_list if num <= n*n]
    answer = sum(center_list)
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")


n3 = 4
ret3 = solution(n3)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret3, ".")

n4 = 5
ret4 = solution(n4)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret4, ".")