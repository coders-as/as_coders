
def solution(numbers, target):
    from itertools import product
    res = []
    
    tmp = [(n, -n) for n in numbers]
    calc = list(product(*tmp))
    
    for c in calc:
        res.append(sum(c))
        
    return res.count(target)
        
