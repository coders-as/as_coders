'''
1. answer를 prices의 길이 n으로 맞춰줍니다.
2. 스택 st를 생성합니다. st는 시간을 쌓습니다.
3. 0초부터 n-1초까지 순회합니다.
   1. st이 비지 않고, 만약 st의 가장 마지막 원소 top이 현재 주식 가격보다 크다면 다음을 반복합니다.
      1. 스택에서 가장 마지막에 저장된 시간 top을 빼냅니다.
      2. answer[top]에 현재시간 i 와 top의 차를 저장합니다.
   2. st에 현재 시간 i를 저장합니다.
4. 스택이 빌 때까지 다음을 반복합니다.
   1. 스택에서 가장 마지막에 저장된 시간 top을 빼냅니다.
   2. answer[top]에 끝 시간 n-1 과 top의 차를 저장합니다.
5. 이렇게 초기화된 answer를 반환합니다.
'''

def solution(prices):
    n = len(prices)
    # 1. answer를 prices 길이와 맞춘다.
    answer = [0] * n
    # 2. 스택 생성
    st = []
    # 3. 0 ~ n-1 초까지 순회
    for i in range(n):
        # 1. 스택 비지 않고, prices[top] > prices[i] 이라면 다음 반복
        # 1-1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 1-2. answer[top]에 i - top을 저장
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top
        # 2. 스택에 현재 시간 i 저장
        st.append(i)
    
    # 4. 만약 스택이 남아있다면, 스택이 빌 때까지 다음 반복
    while st:
        # 1. 스택에서 마지막에 저장된 시간 top 꺼냄
        # 2. answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
        top = st.pop()
        answer[top] = n - 1 - top
    
    return answer