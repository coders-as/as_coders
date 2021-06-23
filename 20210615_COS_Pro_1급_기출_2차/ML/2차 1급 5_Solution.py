#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    #여기에 코드를 작성해주세요.
    answer = 0
    cnt = []
    check = 0
    while len(arr) > check :
        tmp_cnt = 1
        
        for i in range(len(arr)-1) :
            if arr[i] < arr[i+1] :
                tmp_cnt += 1
            else :
                arr = arr[1:]
                break
            check+=1
                
        cnt.append(tmp_cnt)
    answer = max(cnt)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

