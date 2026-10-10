import sys
from collections import Counter

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    grams = [s[i:i+2] for i in range(n - 1)]
    counts = Counter(grams)
    print(counts.most_common(1)[0][0])

if __name__ == '__main__':
    solve()
