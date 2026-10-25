import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        res = [str(x) for x in range(2, n + 1)] + ["1"]
        out.append(" ".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
