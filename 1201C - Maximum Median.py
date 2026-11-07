import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    
    a.sort()
    mid = n // 2
    
    low = a[mid]
    high = a[mid] + k
    ans = low
    
    while low <= high:
        m = (low + high) // 2
        ops = 0
        for i in range(mid, n):
            if m > a[i]:
                ops += m - a[i]
        if ops <= k:
            ans = m
            low = m + 1
        else:
            high = m - 1
            
    print(ans)

if __name__ == '__main__':
    solve()
