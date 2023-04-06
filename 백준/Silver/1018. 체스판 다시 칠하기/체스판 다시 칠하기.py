import sys
input = sys.stdin.readline

M, N = map(int,input().split())

board = []
for i in range(M):
    board.append(input().strip())

chess = ["WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW",
         "WBWBWBWB",
         "BWBWBWBW"]
min = 64
for i in range(M-7):
    for j in range(N-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if chess[k][l] != board[i+k][j+l]:
                    cnt += 1
        if cnt < min:
            min = cnt
        if 64-cnt < min:
            min = 64-cnt
print(min)