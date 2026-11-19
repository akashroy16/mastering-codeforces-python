import sys

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
        s = data[idx + 1]
        f = data[idx + 2]
        idx += 3
        add = 0
        rem = 0
        for i in range(n):
            if s[i] == '0' and f[i] == '1':
                add += 1
            elif s[i] == '1' and f[i] == '0':
                rem += 1
        out.append(str(max(add, rem)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
