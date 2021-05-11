
def sol(n):
    tmp=n
    res = ''
    dic = {0:'1', 1:'2', 2:'4'}
    while tmp!=0:
        tmp -= 1
        p = int(tmp/3)
        q = tmp%3
        res = dic[q] + res
        tmp = p
    return res