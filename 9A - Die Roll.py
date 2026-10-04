import sys
import math

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    y = int(data[0])
    w = int(data[1])
    
    max_val = max(y, w)
    favorable = 6 - max_val + 1
    total = 6
    
    g = math.gcd(favorable, total)
    print(f"{favorable // g}/{total // g}")

if __name__ == '__main__':
    solve()
