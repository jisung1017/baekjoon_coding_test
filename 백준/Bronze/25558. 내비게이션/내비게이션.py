import sys
input = sys.stdin.readline

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve():
    n = int(input())
    
    sx, sy, ex, ey = map(int, input().split())
    
    min_total_dist = float('inf')  
    best_nav_index = 0             
    
    for i in range(1, n + 1):
        m = int(input()) 
        
        current_x, current_y = sx, sy
        current_total_dist = 0
        
        for _ in range(m):
            nx, ny = map(int, input().split())
            current_total_dist += get_dist(current_x, current_y, nx, ny)
            current_x, current_y = nx, ny
            
        current_total_dist += get_dist(current_x, current_y, ex, ey)
        
        if current_total_dist < min_total_dist:
            min_total_dist = current_total_dist
            best_nav_index = i
            
    print(best_nav_index)

if __name__ == "__main__":
    solve()