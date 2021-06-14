#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    move = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
    
    w = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    h = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    pos_new = []
    
    pos_w = pos[0]
    pos_h = pos[1]
    
    for m in move:
        w_idx = w.index(pos_w)+m[0]
        h_idx = h.index(pos_h)+m[1]
        
        if (w_idx>=0) & (w_idx<len(w)) & (h_idx>=0) & (h_idx<len(h)):
            new_w = w[w_idx]
            new_h = h[h_idx]
            pos_new.append(new_w+new_h)
            
    print(pos_new)        
    answer = len(pos_new)
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")