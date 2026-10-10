import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    mapping = {'p': 'q', 'q': 'p', 'w': 'w'}
    for i in range(1, t + 1):
        a = data[i]
        b = "".join(mapping[ch] for ch in reversed(a))
        out.append(b)
    print("\n".join(out))

if __name__ == '__main__':
    solve()
