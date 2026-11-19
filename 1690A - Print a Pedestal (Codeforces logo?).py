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
        idx += 1
        h1 = (n + 2) // 3 + 1
        rem = n - h1
        h2 = (rem + 1) // 2
        h3 = rem - h2
        if h3 == 0:
            h2 -= 1
            h3 += 1
        out.append(f"{h2} {h1} {h3}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
