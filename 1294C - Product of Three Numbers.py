import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        factors = []
        d = 2
        while d * d * d <= n and len(factors) < 2:
            if n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if len(factors) == 2 and n > 1 and n != factors[0] and n != factors[1]:
            out.append("YES")
            out.append(f"{factors[0]} {factors[1]} {n}")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
