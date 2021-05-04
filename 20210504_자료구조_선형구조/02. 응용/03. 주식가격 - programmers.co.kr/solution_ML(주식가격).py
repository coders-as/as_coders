#=================================#
# My answer
#=================================#

def solution(prices):
    answer = []
    
    #--------------------------------------#
    # 1) 가격이 떨어지는 순간 Break
    # 2) 가격이 떨어진 적 없으면 개수-(#번째)
    #--------------------------------------#    
    for i in range(len(prices)) :
        tmp_answer = 0
        for j in range(i+1, len(prices)) :
            if prices[i] > prices[j] :
                tmp_answer = j-i
                break
        if tmp_answer == 0 :
            tmp_answer = len(prices) - (i + 1)
        answer.append(tmp_answer)
    #--------------------------------------#
    # First Try(Example - Pass / TestCase - Fail(Timeout))
    #--------------------------------------#
    
    # for i in range(len(prices)) :
    #     tmp_answer = 0
    #     for j in range(i+1, len(prices)) :
    #         if prices[i] <= prices[j] :
    #             tmp_answer += 1
    #     answer.append(tmp_answer)            
    
    return answer

#=================================#
# Best answer
#=================================#

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer