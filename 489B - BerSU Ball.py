import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    m = int(data[1+n])
    b = [int(x) for x in data[2+n:2+n+m]]
    
    a.sort()
    b.sort()
    
    i = 0
    j = 0
    pairs = 0
    
    while i < n and j < m:
        if abs(a[i] - b[j]) <= 1:
            pairs += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
            
    print(pairs)

if __name__ == '__main__':
    solve()
