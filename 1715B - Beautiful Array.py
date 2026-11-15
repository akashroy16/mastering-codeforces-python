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
        k = int(data[idx + 1])
        b = int(data[idx + 2])
        s = int(data[idx + 3])
        idx += 4
        min_s = k * b
        max_s = k * b + n * (k - 1)
        if s < min_s or s > max_s:
            out.append("-1")
            continue
        res = [0] * n
        res[0] = k * b
        rem = s - min_s
        for i in range(n):
            add = min(rem, k - 1)
            res[i] += add
            rem -= add
        out.append(" ".join(map(str, res)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
