import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1 : n + 1]]
    best_diff = abs(a[0] - a[n - 1])
    ans = (n, 1)
    for i in range(n - 1):
        d = abs(a[i] - a[i + 1])
        if d < best_diff:
            best_diff = d
            ans = (i + 1, i + 2)
    print(f"{ans[0]} {ans[1]}")

if __name__ == '__main__':
    solve()
