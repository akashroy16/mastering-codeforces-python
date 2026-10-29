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
        a = [int(v) for v in data[idx+2:idx+2+n]]
        idx += 2 + n
        
        min_ans = math.ceil(sum(a) / x)
        max_ans = sum(math.ceil(v / x) for v in a)
        out.append(f"{min_ans} {max_ans}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
