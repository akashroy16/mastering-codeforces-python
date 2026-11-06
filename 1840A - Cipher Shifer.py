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
        s = data[idx+1]
        idx += 2
        
        res = []
        i = 0
        while i < n:
            ch = s[i]
            res.append(ch)
            j = i + 1
            while j < n and s[j] != ch:
                j += 1
            i = j + 1
        out.append("".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
