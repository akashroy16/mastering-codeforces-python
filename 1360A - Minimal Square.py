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
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        side = max(min(a, b) * 2, max(a, b))
        out.append(str(side * side))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
