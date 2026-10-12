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
        ops = 0
        for i in range(1, n):
            if a[i] % 2 == a[i-1] % 2:
                ops += 1
        out.append(str(ops))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
