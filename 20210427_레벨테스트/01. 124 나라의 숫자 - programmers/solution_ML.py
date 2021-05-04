def solution(n):
    
    answer = ''
    #-------------------------------------#
    # My Solution)
    # - [Func] : 몫(//), 나머지(%)
    # - (나머지, 숫자) : (1, '1'), (2, '2'), (0, '4')
    #-------------------------------------#
        
    while n > 0:
        if str(n % 3) != '0':
            answer = str(n%3) + answer
        else:
            answer = '4' + answer
            n -= 1
        n //= 3
    return answer
 
    
    
def solution(n):
    #-------------------------------------#
    # Best Solution)
    # - [Func] : divmod(a, b) = 몫, 나머지
    #-------------------------------------#  
    answer = ''
    base_num = ['1', '2', '4']
    while n > 0:
        #----------------------------------------#
        # - ex) n = 13 -> 몫 : 4, 나머지 : 1 -> answer = '111'
        # -     (몫, 나머지) : n=12 -> (4, 0) -> n=3 -> (1, 0)) -> n = 0 -> (0, 0)
        #----------------------------------------#
        n -= 1
        quo, rem = divmod(n, 3)
        answer = base_num[rem] + answer
        n = quo
        
   