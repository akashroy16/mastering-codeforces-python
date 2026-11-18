import sys
from bisect import bisect_left, bisect_right

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        l = int(data[idx + 1])
        r = int(data[idx + 2])
        idx += 3
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        a.sort()
        ans = 0
        for i in range(n):
            left = bisect_left(a, l - a[i], i + 1, n)
            right = bisect_right(a, r - a[i], i + 1, n)
            ans += right - left
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
