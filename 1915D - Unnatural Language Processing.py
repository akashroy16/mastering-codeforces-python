import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    vowels = {'a', 'e'}
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        res = []
        i = n - 1
        while i >= 0:
            if s[i] in vowels:
                res.append(s[i - 1 : i + 1])
                i -= 2
            else:
                res.append(s[i - 2 : i + 1])
                i -= 3
        out.append(".".join(reversed(res)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
