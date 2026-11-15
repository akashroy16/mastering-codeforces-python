import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1 : n + 1]]
    b = [int(x) for x in data[n + 1 : 2 * n + 1]]
    c = sorted(a[i] - b[i] for i in range(n))
    l, r = 0, n - 1
    ans = 0
    while l < r:
        if c[l] + c[r] > 0:
            ans += r - l
            r -= 1
        else:
            l += 1
    print(ans)

if __name__ == '__main__':
    solve()
