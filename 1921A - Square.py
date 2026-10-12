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
        pts = []
        for _ in range(4):
            pts.append((int(data[idx]), int(data[idx+1])))
            idx += 2
        pts.sort()
        side = abs(pts[0][1] - pts[1][1])
        if side == 0:
            side = abs(pts[0][0] - pts[2][0])
        out.append(str(side * side))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
