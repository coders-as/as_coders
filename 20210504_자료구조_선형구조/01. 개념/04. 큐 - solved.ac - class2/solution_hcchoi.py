
def queue():
    n = int(input())
    res = []
    while n:
        comm = input()
        
        if 'push' in comm:
            comm = comm.split(' ')
            if comm[1].isdigit():
                res.append(int(comm[1]))
                
        elif comm=='pop':
            if len(res)!=0:
                print(res[0])
                res.pop(0)
            else:
                print('-1')
            
        elif comm=='size':
            print(len(res))
            
        elif comm=='empty':
            if len(res)!=0:
                print('0')
            else:
                print('1')
            
        elif comm=='front':
            if len(res)!=0:
                print(res[0])
            else:
                print('-1')
            
        elif comm=='back':
            if len(res)!=0:
                print(res[-1])
            else:
                print('-1')
                
        n -= 1
    
    