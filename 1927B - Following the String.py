import sys
import string

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    alphabet = list(string.ascii_lowercase)
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        counts = {i: [] for i in range(n + 1)}
        for char in alphabet:
            counts[0].append(char)
        res = []
        for x in a:
            char = counts[x].pop(0)
            res.append(char)
            counts[x + 1].append(char)
        out.append("".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
