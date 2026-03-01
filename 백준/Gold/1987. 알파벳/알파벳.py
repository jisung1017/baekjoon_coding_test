import sys

input = sys.stdin.readline

R, C = map(int, input().split())
A = [input().rstrip() for _ in range(R)]
board = [[ord(ch)-65 for ch in row] for row in A]


best = 0

def dfs(x, y, mask, depth):
    global best

    if best == 26 :
        return
    if depth > best :
        best = depth

    adj_list = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    for point in adj_list :
        nx, ny = point[0], point[1]
        if 0 <= nx < R and 0 <= ny < C:
            bit = 1 << (board[nx][ny])
            if not (mask & bit) :
                dfs(nx, ny, mask|bit, depth+1)
            
mask = 1 << (board[0][0])
dfs(0, 0, mask, 1)
print(best)
