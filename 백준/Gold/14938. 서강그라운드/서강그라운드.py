import sys
input = sys.stdin.readline
import heapq

def add_graph(graph, a, b, v) :
    graph[a].append((b, v))
    graph[b].append((a, v))

def dijkstra(graph, start) :
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    max_item = 0

    while heap :
        cost, node = heapq.heappop(heap)
        for next_node, next_cost in graph[node] :
            if cost + next_cost <= m and dist[next_node] > cost + next_cost :
                dist[next_node] = cost + next_cost
                heapq.heappush(heap, (next_cost + cost, next_node))
    
    for i in range(1, len(dist)) :
        if dist[i] != float('inf') :
            max_item += t[i]
    
    return max_item

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
t = [0] + list(map(int, input().split()))
for _ in range(r) :
    a, b, l = map(int, input().split())
    add_graph(graph, a, b, l)

res = 0
for i in range(1, n + 1) :
    res = max(res, dijkstra(graph, i))
  
print(res)