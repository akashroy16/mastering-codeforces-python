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
        a = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                a = n // i
                break
            i += 1
        out.append(f"{a} {n - a}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
