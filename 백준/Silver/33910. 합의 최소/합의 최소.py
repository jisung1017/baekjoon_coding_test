N = int(input())
A = list(map(int,input().split()))

cur = A[-1]
res = A[-1]
for i in range(N-2,-1,-1) :
  if A[i] <= cur :
    res += A[i]
    cur = A[i]
  else :
    res += cur
    
print(res)