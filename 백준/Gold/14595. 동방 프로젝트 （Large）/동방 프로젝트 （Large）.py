import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

diff = [0]*(N+2)

for _ in range(M) :
    x, y = map(int,input().split())
    if x < y :
        diff[x] += 1
        diff[y] -= 1

run = 0
walls = 0
for i in range(1, N) :
    run += diff[i]
    if run == 0:
        walls += 1

answer = walls + 1
print(answer)