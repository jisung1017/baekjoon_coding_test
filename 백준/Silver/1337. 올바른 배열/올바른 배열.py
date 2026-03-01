import sys
input = sys.stdin.readline

N = int(input())
A = list(int(input().strip()) for _ in range(N))
A.sort()

ans = 5

j = 0
for i in range(N) :
    while j < N and A[j] <= A[i] + 4 :
        j += 1
    
    have = j - i
    need = 5 - have

    ans = min(ans, need)

print(ans)