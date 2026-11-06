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
        m = int(data[idx+1])
        idx += 2
        if n >= m and (n - m) % 2 == 0:
            out.append("Yes")
        else:
            out.append("No")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
