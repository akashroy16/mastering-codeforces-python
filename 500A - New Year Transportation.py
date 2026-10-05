import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    t = int(data[1])
    a = [int(x) for x in data[2:1+n]]
    
    curr = 1
    while curr < t:
        curr += a[curr - 1]
        
    if curr == t:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()
