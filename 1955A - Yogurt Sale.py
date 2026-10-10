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
        a = int(data[idx+1])
        b = int(data[idx+2])
        idx += 3
        cost1 = n * a
        cost2 = (n // 2) * b + (n % 2) * a
        out.append(str(min(cost1, cost2)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
