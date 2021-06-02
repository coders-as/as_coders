def func_a(string, length):
    padZero = ""
    padSize = length-len(string)#@@@
    for i in range(padSize):
        padZero += "0"
    return padZero + string

def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    binaryA = func_a(binaryA, max_length)
    binaryB = func_a(binaryB, max_length) 
    hamming_distance = 0
#     min_length = min(len(binaryA), len(binaryB)) 
    for i in range(max_length):
        if binaryA[i]!=binaryB[i]:#@@@: #func_a 의 출력에 2를 붙임, min_length변수 생성, 둘 차이만큼 hamming distance 발생하므로
            print(1)
            hamming_distance += 1
    return hamming_distance

#The following is code to output testcase.
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")
