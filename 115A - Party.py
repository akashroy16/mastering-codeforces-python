import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    p = [int(x) for x in data[1:n+1]]
    
    max_depth = 0
    for i in range(1, n + 1):
        depth = 0
        curr = i
        while curr != -1:
            depth += 1
            curr = p[curr - 1]
        max_depth = max(max_depth, depth)
    print(max_depth)

if __name__ == '__main__':
    solve()
