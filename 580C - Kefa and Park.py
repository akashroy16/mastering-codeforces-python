import sys

def solve():
    sys.setrecursionlimit(200000)
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    cats = [int(x) for x in data[2:2+n]]
    
    adj = [[] for _ in range(n + 1)]
    idx = 2 + n
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    valid_restaurants = 0
    stack = [(1, 0, cats[0])]  # (node, parent, consecutive_cats)
    
    while stack:
        u, p, consecutive = stack.pop()
        
        if consecutive > m:
            continue
            
        is_leaf = True
        for v in adj[u]:
            if v != p:
                is_leaf = False
                next_cats = consecutive + 1 if cats[v - 1] == 1 else 0
                stack.append((v, u, next_cats))
                
        if is_leaf:
            valid_restaurants += 1
            
    print(valid_restaurants)

if __name__ == '__main__':
    solve()
