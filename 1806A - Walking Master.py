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
        c = int(data[idx+2])
        d = int(data[idx+3])
        idx += 4
        if d < b or (c - a) > (d - b):
            out.append("-1")
        else:
            out.append(str((d - b) + (d - b + a - c)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
