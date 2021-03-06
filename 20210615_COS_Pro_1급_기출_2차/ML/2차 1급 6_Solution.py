#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    # 여기에 코드를 작성해주세요.
    answer = []
    direction_set = {'U' : [0,1], 'D' : [0,-1], 'L' : [-1, 0], 'R' : [1,0]}
    now_pos = [0, 0]
    for str_dir in commands :
        now_pos = [now_pos[0] + direction_set[str_dir][0], now_pos[1] + direction_set[str_dir][1]]
    answer = now_pos
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")
