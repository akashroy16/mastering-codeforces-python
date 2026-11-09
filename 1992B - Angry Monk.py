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
        idx += 2
        a = [int(x) for x in data[idx : idx + k]]
        idx += k
        a.sort()
        ops = 0
        for i in range(k - 1):
            ops += 2 * a[i] - 1
        out.append(str(ops))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
