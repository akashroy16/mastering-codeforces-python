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
        pts = sorted([int(data[idx]), int(data[idx+1]), int(data[idx+2])])
        idx += 3
        out.append(str(pts[2] - pts[0]))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
