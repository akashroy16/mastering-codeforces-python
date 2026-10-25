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
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        diff = abs(a - b) / 2.0
        out.append(str(math.ceil(diff / c)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
