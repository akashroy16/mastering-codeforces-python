import sys
from collections import Counter

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
        a = data[idx : idx + n]
        idx += n
        score = sum(c // 2 for c in Counter(a).values())
        out.append(str(score))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
