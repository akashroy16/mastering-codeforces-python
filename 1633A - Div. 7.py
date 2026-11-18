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
        if n % 7 == 0:
            out.append(str(n))
        else:
            base = (n // 10) * 10
            for d in range(10):
                if (base + d) % 7 == 0:
                    out.append(str(base + d))
                    break
    print("\n".join(out))

if __name__ == '__main__':
    solve()
