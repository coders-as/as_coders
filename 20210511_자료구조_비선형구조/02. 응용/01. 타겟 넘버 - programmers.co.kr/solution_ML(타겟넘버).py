#=================================#
# My answer
#=================================#
def solution(numbers, target):
    from itertools import product
    #---------------------------------------------------------------#
    # product : cartesian product
    # - ['12','45','78'] => ['147', '148', ...]
    # - generator이므로 무조건 list로 반환하여 저장해야 함
    # - itertools에는 permutaions(list, r), combinations(list, r) 있음
    #---------------------------------------------------------------#
    answer = 0
    numbers_choice = []
    for i in range(len(numbers)) :
        numbers_choice.append((numbers[i], -numbers[i]))
    
    product_comb = list(product(*numbers_choice))
    
    for comb in product_comb :
        if sum(comb) == target :
            answer += 1
    return answer

#=================================#
# Best answer1
#=================================#
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

#=================================#
# Best answer2 (DFS 이용)
#=================================#
def dfs(numbers, idx, value, target):
    ret = 0
    if idx == len(numbers):
        if value == target: return 1
        else: return 0
    ret += dfs(numbers, idx+1, value+numbers[idx], target)
    ret += dfs(numbers, idx+1, value-numbers[idx], target)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer


#=================================#
# Best answer3 (DFS 이용)
#=================================#
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer