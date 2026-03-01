N, new, P = map(int, input().split())
if N == 0 :
    print(1)
    exit()

A = list(map(int, input().split()))
A.sort(reverse=True)

cnt = 1
for x in A :
    if x > new :
        cnt += 1
    else :
        break

if N == P :
    if cnt > P :
        print(-1)
    elif A[-1] == new :
        print(-1)
    else :
        print(cnt)
else :
    print(cnt)
    