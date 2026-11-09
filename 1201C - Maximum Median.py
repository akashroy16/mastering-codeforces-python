import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    a = [int(x) for x in data[2:]]
    a.sort()
    low = a[n // 2]
    high = low + k
    ans = low
    while low <= high:
        mid = (low + high) // 2
        req = 0
        for i in range(n // 2, n):
            if a[i] < mid:
                req += mid - a[i]
        if req <= k:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == '__main__':
    solve()
