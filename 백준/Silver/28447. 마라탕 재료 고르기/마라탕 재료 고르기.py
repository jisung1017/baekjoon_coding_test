import sys
input = sys.stdin.readline
from itertools import combinations

N, K = map(int, input().split())
A= []
for i in range(N) :
    A.append(list(map(int, input().split())))
res = 0

if K == 1 :
    print(0)
    sys.exit()

for x in combinations(range(N), K) :
    sum = 0
    for i in range(K) :
        for j in range(i + 1, K) :
            sum += A[x[i]][x[j]]
    if res == 0 :
        res = sum
    else :
        res = max(res, sum)

print(res)