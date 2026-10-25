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
        neg = sum(1 for x in a if x < 0)
        pos = sum(1 for x in a if x > 0)
        zeros = n - neg - pos
        ops = 0
        if neg % 2 != 0:
            if zeros > 0:
                ops += 1
            else:
                ops += 2
        out.append(str(ops))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
