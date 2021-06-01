
n= [ [7],
    [6],
    [1, 2],
    [2, 3],
    [1, 5],
    [5, 2],
    [5, 6],
    [4, 7]
     ]

check = [1]
len1 = len(check)
len2 = 0

while(len1 !=len2):
    len1 = len(check)
    for i in n:
        if len(i)==2:
            if any(i[0] == num for num in check):
                    check.append(i[1])
    check = set(check)
    check = list(check)
    len2 = len(check)

answer = len(check) -1

print(answer)
