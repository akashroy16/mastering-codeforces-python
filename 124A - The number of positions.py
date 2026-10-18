import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    
    ans = min(n - a, b + 1)
    print(ans)

if __name__ == '__main__':
    solve()
