import sys
import math

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        screens = math.ceil(y / 2)
        rem_cells = screens * 15 - y * 4
        if x > rem_cells:
            screens += math.ceil((x - rem_cells) / 15)
        out.append(str(screens))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
