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
        if n == 1:
            out.append("0")
        elif n == 2:
            out.append(str(m))
        else:
            out.append(str(2 * m))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
