
def alarm(H, M):
    if M > 45:
        adjH = H
        adjM = M-45
    else:
        if H!=0:
            adjH = H-1
            adjM = M + 15
        else:
            adjH = 23
            adjM = M + 15
    return adjH, adjM