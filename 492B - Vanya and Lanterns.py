import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    l = int(data[1])
    a = [int(x) for x in data[2:n+2]]
    
    a.sort()
    
    max_gap = 0
    for i in range(n - 1):
        max_gap = max(max_gap, a[i+1] - a[i])
        
    ans = max(max_gap / 2.0, float(a[0]), float(l - a[-1]))
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()
