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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        neg = a.count(-1)
        pos = n - neg
        ops = 0
        while pos < neg or neg % 2 != 0:
            neg -= 1
            pos += 1
            ops += 1
        out.append(str(ops))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
