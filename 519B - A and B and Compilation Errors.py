import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    b = [int(x) for x in data[n+1:2*n]]
    c = [int(x) for x in data[2*n:3*n-1]]
    
    diff1 = sum(a) - sum(b)
    diff2 = sum(b) - sum(c)
    print(diff1)
    print(diff2)

if __name__ == '__main__':
    solve()
