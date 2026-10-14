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
        x = int(data[idx])
        y = int(data[idx+1])
        a = int(data[idx+2])
        b = int(data[idx+3])
        idx += 4
        cost1 = (x + y) * a
        cost2 = min(x, y) * b + abs(x - y) * a
        out.append(str(min(cost1, cost2)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
