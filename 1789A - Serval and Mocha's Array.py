import sys
from math import gcd

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
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        possible = False
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(a[i], a[j]) <= 2:
                    possible = True
                    break
            if possible:
                break
        out.append("Yes" if possible else "No")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
