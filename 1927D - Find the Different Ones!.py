import sys

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
        idx += 1
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        prev = [-1] * n
        for i in range(1, n):
            if a[i] != a[i - 1]:
                prev[i] = i - 1
            else:
                prev[i] = prev[i - 1]
        q = int(data[idx])
        idx += 1
        for _ in range(q):
            l = int(data[idx]) - 1
            r = int(data[idx + 1]) - 1
            idx += 2
            if prev[r] >= l:
                out.append(f"{prev[r] + 1} {r + 1}")
            else:
                out.append("-1 -1")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
