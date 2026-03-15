import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

B = []
B.append(A[1]-1)
for i in range(2,N) :
    is_vaild = True
    for x in B :
        if A[i] % x == 1 :
            is_vaild=False
            break    
    if is_vaild : B.append(A[i]-1)

print(len(B))
