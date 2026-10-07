import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    
    ans = min(abs(x) for x in a)
    print(ans)

if __name__ == '__main__':
    solve()
