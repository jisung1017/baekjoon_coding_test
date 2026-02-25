import sys, heapq
input = sys.stdin.readline
from collections import deque

def eat(start_x, start_y):
    q = deque([(start_x, start_y, 0)])
    heap = []
    visited = [[False] * N for _ in range(N)]
    visited[start_x][start_y] = True

    min_dist = float('inf')

    while q:
        x, y, dist = q.popleft()

        if dist > min_dist:
            break

        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if A[nx][ny] <= shark_size: 
                    visited[nx][ny] = True

                    if 0 < A[nx][ny] < shark_size:
                        min_dist = dist + 1
                        heapq.heappush(heap, (dist + 1, nx, ny))
                    else:
                        if dist + 1 <= min_dist:
                            q.append((nx, ny, dist + 1))

    return heap[0] if heap else None

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if A[i][j] == 9 :
            shark = (i, j)
            A[i][j] = 0

shark_size = 2
time = 0
grow = 0

while True :
    eat_fish = eat(shark[0], shark[1])
    if eat_fish is None :
        break

    time += eat_fish[0]
    grow += 1
    A[eat_fish[1]][eat_fish[2]] = 0
    shark = (eat_fish[1], eat_fish[2])
    if grow == shark_size :
        shark_size += 1
        grow = 0

print(time)