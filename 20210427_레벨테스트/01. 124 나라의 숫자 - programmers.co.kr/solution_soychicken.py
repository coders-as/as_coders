
def solution(n):
    k = ''
    while n>0:
        if n%3==0:
            k = k+str(4)
        if n%3==1:
            k = k+str(1)
        if n%3==2:
            k = k+str(2)
        n = int((n-1)/3)
    answer = ''.join(reversed(k))
    return answer
