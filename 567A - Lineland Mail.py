import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    x = [int(v) for v in data[1 : n + 1]]
    out = []
    for i in range(n):
        if i == 0:
            mn = x[1] - x[0]
        elif i == n - 1:
            mn = x[n - 1] - x[n - 2]
        else:
            mn = min(x[i] - x[i - 1], x[i + 1] - x[i])
        mx = max(x[i] - x[0], x[n - 1] - x[i])
        out.append(f"{mn} {mx}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
