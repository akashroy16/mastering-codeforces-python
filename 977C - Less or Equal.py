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
    if k == 0:
        if a[0] > 1:
            print(a[0] - 1)
        else:
            print("-1")
    else:
        ans = a[k - 1]
        if k < n and a[k] == ans:
            print("-1")
        else:
            print(ans)

if __name__ == '__main__':
    solve()
