
def dfs(node) :
    global cnt
    child_exist = False
    if node == x :
        return

    for child in tree[node] :
        if child == x :
            continue
        child_exist = True
        dfs(child)  
    
    if not child_exist :
        cnt += 1

N = int(input())
A = list(map(int, input().split()))
x = int(input())

tree = [[] for _ in range(N)]

for i in range(N) :
    p = A[i]
    if p != -1 :
        tree[p].append(i)

cnt = 0
for i in range(N) :
    if A[i] == -1 :
        root = i
        break

dfs(root)
print(cnt)