import sys
import math

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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        possible = False
        for i in range(n):
            for j in range(i + 1, n):
                if math.gcd(a[i], a[j]) <= 2:
                    possible = True
                    break
            if possible:
                break
                
        if possible:
            out.append("Yes")
        else:
            out.append("No")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
