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
        b = [n + 1 - x for x in a]
        out.append(" ".join(map(str, b)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
