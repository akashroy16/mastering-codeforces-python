import sys

def solve():
    input = sys.stdin.read
    lines = input().split()
    if not lines:
        return
    t = int(lines[0])
    out = []
    for k in range(1, t + 1):
        s = lines[k]
        c0 = s.count('0')
        c1 = s.count('1')
        ans = len(s)
        for i in range(len(s)):
            if s[i] == '0':
                if c1 > 0:
                    c1 -= 1
                else:
                    ans = len(s) - i
                    break
            else:
                if c0 > 0:
                    c0 -= 1
                else:
                    ans = len(s) - i
                    break
        else:
            ans = 0
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
