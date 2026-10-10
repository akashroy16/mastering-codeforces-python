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
        x, y = 0, 0
        passed = False
        for ch in s:
            if ch == 'L': x -= 1
            elif ch == 'R': x += 1
            elif ch == 'U': y += 1
            elif ch == 'D': y -= 1
            if x == 1 and y == 1:
                passed = True
                break
        if passed:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
