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
        p1 = data[idx : idx + n]
        idx += n
        p2 = data[idx : idx + n]
        idx += n
        p3 = data[idx : idx + n]
        idx += n
        counts = Counter(p1 + p2 + p3)
        pts = [0, 0, 0]
        for i, p in enumerate([p1, p2, p3]):
            for word in p:
                if counts[word] == 1:
                    pts[i] += 3
                elif counts[word] == 2:
                    pts[i] += 1
        out.append(f"{pts[0]} {pts[1]} {pts[2]}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
