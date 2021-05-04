

import copy

def rotate(m):
    N = len(m)
    box = [[0] * N for x in range(N)]
    for r in range(N):
        for c in range(N):
            box[r][c] = m[c][-1 - r]
    return box


N = len(lock)
M = len(key)


def check_lock(lock_x, lock_y, lock, key):
    lock_tmp = copy.deepcopy(lock)
    for key_y in range(N):
        for key_x in range(N):
            if 0 <=(key_x + lock_x) < M and 0<=(key_y + lock_y) < M :
                lock_tmp[key_x + lock_x][key_y + lock_y] = lock_tmp[key_x + lock_x][key_y + lock_y] + key[key_x][key_y]
    box = [[1] * N for x in range(N)]

    if lock_tmp == box:
        return True
    else:
        return False

def solution(key, lock):

    rot = 0
    answer = False
    for rot in range(4):
        key = rotate(key)
        lock_y=0
        lock_x=0
        for lock_y in range(0-M, M+1):
            for lock_x in range(0-M, M+1):
                answer = check_lock(lock_x,lock_y,lock,key)
                if answer == True:
                    return answer

    return answer

answer = solution(key, lock)
