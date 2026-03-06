x = int(input())
A = list(map(int, input().split()))
cnt = 0

for ch in A :
    if (ch%10) == x :
        cnt += 1
print(cnt)