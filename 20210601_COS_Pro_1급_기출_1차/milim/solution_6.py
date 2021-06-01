#You may use import as below.
#import math

def solution(pos):
    
    alpha_dict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' :6, 'H' : 7}
    start = (alpha_dict[pos[0]], int(pos[1])-1)
    
    move_list = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]
    answer = 0
    # Write code here.
    for i in range(len(move_list)) :
        if ((0 <= start[0] + move_list[i][0] < len(alpha_dict)) &
            (0 <= start[1] + move_list[i][1] < len(alpha_dict))) :
            answer += 1
    
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")