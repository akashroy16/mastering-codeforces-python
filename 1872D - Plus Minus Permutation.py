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
        x = int(data[idx+1])
        y = int(data[idx+2])
        idx += 3
        
        common = n // (x * y // math.gcd(x, y))
        count_x = n // x - common
        count_y = n // y - common
        
        sum_x = count_x * (2 * n - count_x + 1) // 2
        sum_y = count_y * (count_y + 1) // 2
        out.append(str(sum_x - sum_y))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
