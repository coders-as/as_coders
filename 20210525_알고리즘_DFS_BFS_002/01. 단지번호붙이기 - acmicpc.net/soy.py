import numpy
import copy
input = [7,"0110100","0110101","1110101","0000111","0100000","0111110","0111000"]


main = []
for i in input[1:]:
    i = list(i)
    main.append(i)

max_length = input[0]


summary=[] 

def fn_check(k):
    z1 = copy.deepcopy(k)
    for m in z1:
        i = m[0]
        j = m[1]
        if (j != 0) & (main[i][j - 1] == '1'):
            k.append([i, j - 1])
        if (i != 0) & (main[i - 1][j] == '1'):
            k.append([i - 1, j])
        if (i != (max_length - 1)):
            if (main[i + 1][j] == '1'):
                k.append([i + 1, j])
        if (j != (max_length - 1)):
            if main[i][j + 1] == '1':
                k.append([i, j + 1])
    zone1 = numpy.unique(k, axis=0)
    zone1 = list(zone1)
    return zone1

for i in range(max_length):
    for j in range(max_length):
        if main[i][j] =='1':
            zone1 = [[i,j]]
            count1 = len(zone1)
            count2 = count1+1
            while count1<count2:
                count1 = len(zone1)
                zone1 = fn_check(zone1)
                count2 = len(zone1)
            summary.append(len(zone1))
            for k in zip(zone1):
                i = k[0][0]
                j = k[0][1]
                main[i][j] = '0'


result = [len(summary)] + sorted(summary)
print(result)
