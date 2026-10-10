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
        l = int(data[idx])
        r = int(data[idx+1])
        idx += 2
        if 2 * l <= r:
            out.append(f"{l} {2 * l}")
        else:
            out.append("-1 -1")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
