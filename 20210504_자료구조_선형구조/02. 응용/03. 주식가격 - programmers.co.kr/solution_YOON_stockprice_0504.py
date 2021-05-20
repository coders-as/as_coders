# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

input=[1,2,3,2,3]
return00=[]
def solution_YOON_stockprice_0504(input):
    for i in range(len(input)) :
        cnt=0
        k= len(input)-i
        print(k)
        for j in range(1,k):
            if input[i]<=input[i+j] :
                cnt=cnt+1
            else :
                cnt=cnt

        return00.append(cnt)
    print(return00)
if __name__ == '__main__':
    solution_YOON_stockprice_0504(input)
    print('Done')
